# -*- coding: utf-8 -*-
import wx
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
        self.top_trans_text.SetLabel('FES')
        self.top_trans_text.SetForegroundColour((0, 0, 255))

    def on_choose_tran_type(self, event):
        choice_num = self.trans_choice.GetCurrentSelection()
        if choice_num == 0:
            self.settle_type, self.org_nick_name = ('', '')
            return
        else:
            self.settle_type, self.org_nick_name, choice_type = self.trans_choice_dict.get(choice_num)

    def on_change_date(self, event):
        self.tran_date = self.trans_date_picker.GetValue().Format('%Y%m%d')

    def on_get_status(self, event):
        if not self.settle_type:
            wx.MessageBox('未选择交易类型！')
            self.trans_choice.SetFocus()
            return
        try:
            if not self.amt_text_ctrl.GetValue():
                wx.MessageBox('总金额不能为空！')
                return
            self.total_amt = float(self.amt_text_ctrl.GetValue())
        except ValueError:
            wx.MessageBox('请输入正确的总金额数字！')
            self.amt_text_ctrl.Clear()
            self.amt_text_ctrl.SetFocus()
            return
        status = self.fb.check_status(self.tran_date, self.settle_type, self.org_nick_name, self.total_amt)
        print(status)

