# -*- coding: utf-8 -*-
from fbui.rootframe import RootFrame
from fesbusi import FesBusi


class FesRootFrame(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fb = FesBusi()

        self.trans_choice_dict = {
            0: (),
            1: ('5', 'GHPOS', '工商银行大厅POS'),
            2: ('6', 'GHIMAC', '工商银行一体机IMAC'),
            3: ('8', 'GHAPP', '工商银行APP'),
            4: ('5', 'ZHPOS', '招商银行大厅POS'),
            5: ('8', 'CCBAPP', '建设银行APP')
        }
        self.total_amt = 0
        self.tran_date = ''
        self.settle_type = ''
        self.org_nick_name = ''
        self.init_widgets()

    def init_widgets(self):
        self.top_static_text.SetLabel('未选择交易类型！')
        self.top_static_text.SetForegroundColour((255, 0, 0))
        self.status_button.Disable()
        self.check_account_button.Disable()
        self.settle_button.Disable()
        self.write_back_button.Disable()

    def on_amt_button(self, event):
        pass

    def on_choose_tran_type(self, event):
        choice_num = self.trans_choice.GetCurrentSelection()
        if choice_num == 0:
            self.top_static_text.SetLabel('未选择交易类型！')
            self.top_static_text.SetForegroundColour((255, 0, 0))
            self.status_button.Disable()
            return

        self.tran_date = self.trans_date_picker.GetValue().Format('%Y-%m-%d')
        self.settle_type, self.org_nick_name, choice_type = self.trans_choice_dict.get(choice_num)
        self.top_static_text.SetLabel(choice_type + '  ' + self.tran_date)
        self.top_static_text.SetForegroundColour((0, 0, 255))
        if self.total_amt and self.tran_date and self.settle_type and self.org_nick_name:
            self.status_button.Enable()

    def on_get_status(self, event):
        status = self.fb.check_account(self.tran_date, self.settle_type, self.org_nick_name)
        print(status)


