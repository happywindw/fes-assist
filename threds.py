import wx
from wx.lib.pubsub import pub
from threading import Thread
from fesbusi import FesBusi


class B9999Thread(Thread):
    def __init__(self, bank_code, start_date, end_date):
        Thread.__init__(self)
        self.bank_code = bank_code
        self.start_date = start_date
        self.end_date = end_date
        self.start()

    def run(self):
        result = FesBusi.post_b9999(self.bank_code, self.start_date, self.end_date)
        wx.CallAfter(pub.sendMessage, 'download', result=result)
