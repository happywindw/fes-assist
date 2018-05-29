import threading
import wx

from wx.lib.pubsub import pub
from fesbusi import FesBusi


class ExceptionThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.flag = True
        self.exception = ()
        self.event = threading.Event()
        self.start()

    def run(self):
        while self.flag:
            self.event.wait()
            if self.flag:
                wx.CallAfter(pub.sendMessage, 'exception', exception=self.exception)
                self.event.clear()

    def show_exception(self, e):
        self.exception = e
        self.event.set()

    def exit_thread(self):
        self.flag = False
        self.event.set()


class B9999Thread(threading.Thread):
    def __init__(self, bank_account, start_date, end_date):
        threading.Thread.__init__(self)
        self.bank_account = bank_account
        self.start_date = start_date
        self.end_date = end_date
        self.start()

    def run(self):
        result = FesBusi.post_b9999(self.bank_account, self.start_date, self.end_date)
        wx.CallAfter(pub.sendMessage, 'download', result=result)
