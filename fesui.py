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
        self.total_amt = 0.0
        self.tran_date = self.trans_date_picker.GetValue().Format('%Y-%m-%d')
        self.settle_type = ''
        self.org_nick_name = ''
        self.init_widgets()

    def init_widgets(self):
        self.top_trans_text.SetLabel('未选择交易类型！')
        self.top_trans_text.SetForegroundColour((255, 0, 0))
        self.top_date_text.SetLabel('交易日期：' + self.trans_date_picker.GetValue().Format('%Y-%m-%d'))
        self.top_date_text.SetForegroundColour((0, 0, 255))
        self.top_amt_text.SetLabel('未设置交易总金额！')
        self.top_amt_text.SetForegroundColour((255, 0, 0))

    def on_choose_tran_type(self, event):
        choice_num = self.trans_choice.GetCurrentSelection()
        if choice_num == 0:
            self.settle_type, self.org_nick_name = ('', '')
            self.top_trans_text.SetLabel('未选择交易类型！')
            self.top_trans_text.SetForegroundColour((255, 0, 0))
            return

        self.settle_type, self.org_nick_name, choice_type = self.trans_choice_dict.get(choice_num)
        self.top_trans_text.SetLabel(choice_type)
        self.top_trans_text.SetForegroundColour((0, 0, 255))

    def on_change_date(self, event):
        self.tran_date = self.trans_date_picker.GetValue().Format('%Y%m%d')
        self.top_date_text.SetLabel('交易日期：' + self.trans_date_picker.GetValue().Format('%Y-%m-%d'))

    def on_amt_button(self, event):
        if self.amt_text_ctrl.GetValue():
            self.total_amt = float(self.amt_text_ctrl.GetValue())
            self.top_amt_text.SetLabel('总金额：' + str(self.total_amt) + '元')
            self.top_amt_text.SetForegroundColour((0, 0, 255))
        else:
            self.total_amt = 0.0
            self.top_amt_text.SetLabel('总金额不能为空！')
            self.top_amt_text.SetForegroundColour((255, 0, 0))

    def on_get_status(self, event):
        status = self.fb.check_status(self.tran_date, self.settle_type, self.org_nick_name, self.total_amt)
        print(status)

