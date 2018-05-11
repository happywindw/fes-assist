# -*- coding: utf-8 -*-
import wx
from fbui.rootframe import RootFrame
from fesbusi import FesBusi


class FesRootFrame(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fb = FesBusi()
        self.rgb_dict = {
            'Black': (0, 0, 0),
            'White': (255, 255, 255),
            'Red': (255, 0, 0),
            'Blue': (0, 0, 255),
            'LimeGreen': (50, 205, 50),
            'Gold': (255, 215, 0)
        }

        self.trans_choice_dict = {
            0: ('', ''),
            1: ('5', 'GHPOS'),
            2: ('6', 'GHIMAC'),
            3: ('8', 'GHAPP'),
            4: ('5', 'ZHPOS'),
            5: ('8', 'CCBAPP')
        }
        self.total_amt = 0.0
        self.tran_date = self.trans_date_picker.GetValue().Format('%Y%m%d')
        self.settle_type = ''
        self.org_nick_name = ''

        self.is_check = False
        self.is_settle = False
        self.is_confirm = False

        self.top_trans_text.SetLabel('FES')
        self.top_trans_text.SetForegroundColour(self.rgb_dict['Blue'])
        self.reset_status()

    def on_choose_tran_type(self, event):
        s, o = self.trans_choice_dict.get(self.trans_choice.GetCurrentSelection())
        if self.settle_type != s or self.org_nick_name != o:
            self.settle_type, self.org_nick_name = s, o
            self.reset_status()

    def on_change_date(self, event):
        td = self.trans_date_picker.GetValue().Format('%Y%m%d')
        if self.tran_date != td:
            self.tran_date = td
            self.reset_status()

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
        s_date = self.trans_date_picker.GetValue().Format('%Y年%m月%d日   ')
        self.top_trans_text.SetLabel(s_date + self.org_nick_name + '  总金额：' + str(self.total_amt))
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROWWAIT))
        self.reset_status()
        self.get_and_show_status(self.total_amt)
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))

    def on_ca_button(self, event):
        """
        用户点击对账按钮
        :param event:
        :return:
        """
        re_check = self.fb.post_check_account(self.tran_date, self.settle_type, self.org_nick_name)
        if re_check:  # 已经对过账，不能重复对账
            wx.MessageBox('不能重复对账！')
        self.get_and_show_status(self.total_amt)

    def on_ca_detail(self, event):
        pass

    def on_cs_button(self, event):
        """
        用户点击清算按钮
        :param event:
        :return:
        """
        re_settle = self.fb.post_check_settle(self.tran_date, self.settle_type, self.org_nick_name)
        if re_settle:  # 已经清算过，不能重复清算
            wx.MessageBox('不能重复清算！')
        self.get_and_show_status(self.total_amt)

    def on_cc_button(self, event):
        event.Skip()

    def reset_status(self):
        self.ca_static_text.SetLabel('未对账')
        self.ca_static_text.Disable()
        self.ca_button.Disable()
        self.ca_grid.ClearGrid()
        self.ca_grid.AutoSize()
        self.ca_detail_text.Hide()
        self.ca_detail_button.Hide()

        self.cs_static_text.SetLabel('未清算')
        self.cs_static_text.Disable()
        self.cs_button.Disable()
        self.cs_grid.ClearGrid()
        self.cs_grid.AutoSize()
        self.cs_detail_text.Hide()
        self.cs_detail_button.Hide()

        self.cc_static_text.SetLabel('未到账')
        self.cc_static_text.Disable()
        self.cc_button.Disable()
        self.cc_grid.ClearGrid()
        self.cc_grid.AutoSize()
        self.cc_detail_text.Hide()
        self.cc_detail_button.Hide()

    def get_and_show_status(self, total_amt):
        """
        获取并显示当日当前业务的对账清算到账状态
        :param total_amt:
        :return:
        """
        status_dict = self.fb.check_status(self.tran_date, self.settle_type, self.org_nick_name)
        print(status_dict)
        if status_dict.get('no_business'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('无业务')
            self.ca_static_text.SetForegroundColour(self.rgb_dict['Black'])
        elif status_dict.get('unchecked'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('未对账')
            if status_dict.get('repeat_aae076'):
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.SetLabel('对账文件笔数和更\n新笔数不一致!')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
            elif self.get_total_amt(status_dict.get('unchecked')) == total_amt:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Blue'])
            else:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.SetLabel('金额不一致!')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
            self.ca_button.Enable()
            self.insert_into_gird(self.ca_grid, status_dict.get('unchecked'))
        elif status_dict.get('checked'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('已对账')
            if status_dict.get('check_diff'):
                self.ca_detail_text.SetLabel('存在单边账!')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
            if self.get_total_amt(status_dict.get('checked')) == total_amt:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['LimeGreen'])
            else:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.SetLabel('对账金额与总\n金额不一致!')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
            self.insert_into_gird(self.ca_grid, status_dict.get('checked'))

        if status_dict.get('unsettled'):
            self.cs_static_text.Enable()
            self.cs_static_text.SetLabel('未清算')
            self.cs_static_text.SetForegroundColour(self.rgb_dict['Blue'])
            self.cs_button.Enable()
        elif status_dict.get('settled'):
            self.cs_static_text.Enable()
            self.cs_static_text.SetLabel('已清算')
            if self.get_total_amt(status_dict.get('settled')) == total_amt:
                self.cs_static_text.SetForegroundColour(self.rgb_dict['LimeGreen'])
            else:
                self.cs_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.cs_detail_text.SetLabel('清算金额与总\n金额不一致!')
                self.cs_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.cs_detail_text.Show()
                self.cs_detail_button.Show()
            self.insert_into_gird(self.cs_grid, status_dict.get('settled'))

        if status_dict.get('unconfirmed'):
            self.cc_static_text.Enable()
            self.cc_static_text.SetLabel('未到账')
            self.cc_static_text.SetForegroundColour(self.rgb_dict['Blue'])
        elif status_dict.get('confirmed'):
            self.cc_static_text.Enable()

            self.cc_static_text.SetLabel('已到账')
            if self.get_total_amt(status_dict.get('confirmed')) == total_amt:
                self.cc_static_text.SetForegroundColour(self.rgb_dict['LimeGreen'])
            else:
                self.cc_static_text.SetForegroundColour(self.rgb_dict['Gold'])
            self.insert_into_gird(self.cc_grid, status_dict.get('confirmed'))
        self.Layout()

    @staticmethod
    def get_total_amt(data):
        if not len(data):
            return 0
        total = 0.0
        for row in data:
            total += float(row[0])
        return total

    @staticmethod
    def insert_into_gird(grid, data, row_labels=None, col_labels=None):
        if not len(data):
            return
        row_num, col_num = len(data), len(data[0])
        grid_row_num = grid.GetNumberRows()
        grid_col_num = grid.GetNumberCols()

        # 设置行数与列数使之与数据匹配
        if row_num > grid_row_num:
            grid.AppendRows(row_num - grid_row_num)
        if row_num < grid_row_num:
            grid.DeleteRows(row_num, grid_row_num - row_num)
        if col_num > grid_col_num:
            grid.AppendCols(col_num - grid_col_num)
        if col_num < grid_col_num:
            grid.DeleteCols(col_num, grid_col_num - col_num)

        # 设置各行、列的标题
        if row_labels and len(row_labels) == row_num:
            for i, lab in enumerate(row_labels):
                grid.SetRowLabelValue(i, lab)
        if col_labels and len(col_labels) == col_num:
            for j, lab in enumerate(col_labels):
                grid.SetColLabelValue(j, lab)

        # 填充数据
        for j, row in enumerate(data):
            for i, ele in enumerate(row):
                grid.SetCellValue(j, i, str(ele))
        grid.AutoSize()
