# -*- coding: utf-8 -*-
import wx
from fbui.rootframe import RootFrame
from fesbusi import FesBusi


class FesRootFrame(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fb = FesBusi()

        self.trans_choice_dict = {
            0: ('', ''),
            1: ('5', 'GHPOS'),
            2: ('6', 'GHIMAC'),
            3: ('8', 'GHAPP'),
            4: ('5', 'ZHPOS'),
            5: ('8', 'CCBAPP')
        }
        self.total_amt = 0.0
        self.tran_date = self.trans_date_picker.GetValue().Format('%Y-%m-%d')
        self.settle_type = ''
        self.org_nick_name = ''

        self.is_check = False
        self.is_settle = False
        self.is_confirm = False

        self.top_trans_text.SetLabel('FES')
        self.top_trans_text.SetForegroundColour((0, 0, 255))
        self.disable_status()

    def on_choose_tran_type(self, event):
        s, o = self.trans_choice_dict.get(self.trans_choice.GetCurrentSelection())
        if self.settle_type != s or self.org_nick_name != o:
            self.settle_type, self.org_nick_name = s, o
            self.disable_status()

    def on_change_date(self, event):
        td = self.trans_date_picker.GetValue().Format('%Y%m%d')
        if self.tran_date != td:
            self.tran_date = td
            self.disable_status()

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
        status_dict = self.fb.check_status(self.tran_date, self.settle_type, self.org_nick_name, self.total_amt)
        self.show_status(status_dict)

    def disable_status(self):
        self.ca_static_text.SetLabel('未对账')
        self.ca_static_text.Disable()
        self.ca_button.Disable()
        self.ca_grid.ClearGrid()

        self.cs_static_text.SetLabel('未清算')
        self.cs_static_text.Disable()
        self.cs_button.Disable()

        self.cc_static_text.SetLabel('未到账')
        self.cc_static_text.Disable()
        self.cc_button.Disable()

    def show_status(self, status_dict):
        print(status_dict)
        if status_dict.get('no_business'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('无业务')
            self.ca_static_text.SetForegroundColour((0, 0, 255))
            self.ca_button.Disable()
        elif status_dict.get('unchecked'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('未对账')
            self.ca_static_text.SetForegroundColour((255, 0, 0))
            self.ca_button.Enable()
            self.ca_grid.SetCellValue(0, 0, str(status_dict.get('unchecked')[0]))
            self.ca_grid.SetCellValue(0, 1, str(status_dict.get('unchecked')[1]))
        elif status_dict.get('checked'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('已对账')
            self.ca_static_text.SetForegroundColour((0, 255, 0))
            self.ca_button.Disable()
            self.ca_grid.SetCellValue(0, 0, str(status_dict.get('checked')[0]))
            self.ca_grid.SetCellValue(0, 1, str(status_dict.get('checked')[1]))

        if status_dict.get('unsettled'):
            self.cs_static_text.Enable()
            self.cs_static_text.SetLabel('未清算')
            self.cs_static_text.SetForegroundColour((255, 0, 0))
            self.cs_button.Enable()
        elif status_dict.get('settled'):
            self.cs_static_text.Enable()
            self.cs_static_text.SetLabel('已清算')
            self.cs_static_text.SetForegroundColour((0, 255, 0))
            self.cs_button.Disable()

        if status_dict.get('unconfirmed'):
            self.cc_static_text.Enable()
            self.cc_static_text.SetLabel('未到账')
            self.cc_static_text.SetForegroundColour((255, 0, 0))
            self.cc_button.Disable()
        elif status_dict.get('confirmed'):
            self.cc_static_text.Enable()
            self.cc_static_text.SetLabel('已到账')
            self.cc_static_text.SetForegroundColour((0, 255, 0))
            self.cc_button.Disable()

    def on_ca_button(self, event):
        self.fb.post_check_account(self.tran_date, self.org_nick_name)

    def on_cs_button(self, event):
        self.fb.post_check_settle(self.tran_date, self.settle_type, self.org_nick_name)

    def on_cc_button(self, event):
        event.Skip()
