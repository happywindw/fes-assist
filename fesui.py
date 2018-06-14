# -*- coding: utf-8 -*-
import datetime
import os
import wx
from wx.lib.pubsub import pub

from fbui.aae076dialog import Aae076Dialog
from fbui.b9999dialog import B9999Dialog
from fbui.dailydialog import DailyDialog
from fbui.delchkdialog import DelChkDialog
from fbui.rootframe import RootFrame
from fesbusi import FesBusi
from feslogs import logger
from settings import TRANS_ACCOUNT
from uithreads import ExceptionThread, B9999Thread
from utils import insert_into_gird


class FesDelChkDialog(DelChkDialog):
    def __init__(self, parent):
        super().__init__(parent)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)


class FesB9999Dialog(B9999Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        choice_list = []
        for k, v in TRANS_ACCOUNT.items():
            choice_list.append(k + ':' + v[1])
        self.bank_choice.SetItems(choice_list)
        self.bank_choice.SetSelection(0)

        self.__bank_account = ()
        self.__start_date = ''
        self.__end_date = ''

    def get_selection(self):
        return self.__bank_account, self.__start_date, self.__end_date

    def on_ok(self, event):
        if self.bank_choice.GetCurrentSelection() == -1:
            wx.MessageBox('请选择一个银行过渡户！')
            return
        else:
            self.__bank_account = TRANS_ACCOUNT[self.bank_choice.GetString(
                self.bank_choice.GetCurrentSelection()).split(':')[0]]
        self.__start_date = self.sd_date_picker.GetValue().Format('%Y%m%d')
        self.__end_date = self.ed_date_picker.GetValue().Format('%Y%m%d')
        if self.__start_date > self.__end_date:
            wx.MessageBox('开始日期不能大于结束日期！')
            return
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)


class FesAae076Dialog(Aae076Dialog):
    def __init__(self, parent, fb, td, st, onn, ra):
        super().__init__(parent)
        self.fb = fb
        self.tran_date = td
        self.settle_type = st
        self.org_nick_name = onn
        self.repeat_aae076 = ra
        self.aae076_detail = [('', '', '', '', '')]

        self.info_text.SetLabel(self.tran_date + '   ' + self.org_nick_name + '   ')
        self.fill_gird()

    def fill_gird(self):
        insert_into_gird(self.aae076_grid, self.repeat_aae076)
        self.aae076_grid.AutoSize()
        insert_into_gird(self.detail_grid, self.aae076_detail)
        self.detail_grid.AutoSize()
        self.Layout()

    def on_get_repeat_aae076(self, event):
        self.repeat_aae076 = self.fb.get_repeat_aae076(self.tran_date, self.org_nick_name)
        if not self.repeat_aae076:
            self.repeat_aae076 = [('', '', '')]
        self.aae076_detail = [('', '', '', '', '')]
        self.fill_gird()

    def on_show_details(self, event):
        selected_rows = event.GetEventObject().SelectedRows
        if selected_rows and self.repeat_aae076:
            aae076 = self.repeat_aae076[selected_rows[0]][1]
            self.aae076_detail = self.fb.get_re_aae076_detail(aae076)
            self.fill_gird()

    def on_delete_row(self, event):
        selected_rows = event.GetEventObject().SelectedRows
        if not selected_rows:
            return
        row_id = self.aae076_detail[selected_rows[0]][3]
        msg = "确定从FES_ONLINE_DETAIL表中删除ID为'%s'的记录？" % row_id
        md = wx.MessageDialog(None, msg, '删除AAE076重复的记录', wx.YES_NO | wx.ICON_QUESTION)
        if md.ShowModal() == wx.ID_YES:
            result = self.fb.delete_re_aae076(row_id)
            if not result:
                md.Destroy()
                wx.MessageBox('删除成功！')
            else:
                md.Destroy()
                wx.MessageBox('删除异常：%s' % result[0][1])
        else:
            md.Destroy()


class FesDailyDialog(DailyDialog):
    def __init__(self, parent):
        super().__init__(parent)
        pass

    def on_ok(self, event):
        event.Skip()


class FesRootFrame(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        icon = wx.Icon('resource/fes.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.et = ExceptionThread()
        self.fb = FesBusi(self.et)

        self.rgb_dict = {
            'Black': (0, 0, 0),
            'White': (255, 255, 255),
            'Red': (255, 0, 0),
            'Blue': (0, 0, 255),
            'LimeGreen': (50, 205, 50),
            'Gold': (255, 215, 0)
        }
        self.btn_code_dict = {
            'ca_button': 0,
            'cs_button': 0,
            'cc_button': 0
        }

        self.trans_choice_dict = {
            0: ('', ''),
            1: ('5', 'GHPOS'),
            2: ('6', 'GHIMAC'),
            3: ('8', 'GHAPP'),
            4: ('5', 'ZHPOS'),
            5: ('5', 'CCBPOS'),
            6: ('8', 'CCBAPP')
        }
        self.total_amt = 0.0
        self.tran_date = self.trans_date_picker.GetValue().Format('%Y%m%d')
        self.settle_type = ''
        self.org_nick_name = ''

        self.is_check = False
        self.is_settle = False
        self.is_confirm = False
        self.status = {}

        self.top_trans_text.SetLabel('FES')
        self.top_trans_text.SetForegroundColour(self.rgb_dict['Blue'])
        self.reset_status()
        pub.subscribe(self.finish_download, 'download')
        pub.subscribe(self.show_exception, 'exception')
        self.Bind(wx.EVT_CLOSE, self.on_close)
        logger.info('Start program...')

    def on_close(self, event):
        if self.et.is_alive():
            self.et.exit_thread()
        logger.info('Exit program.')
        event.Skip()

    def finish_download(self, result):
        print(result)
        if result[0]:
            self.status_bar.SetStatusText('', 1)
            dlg = wx.MessageDialog(None, '成功下载文件%s\n是否立即打开？' % result[1], '文件下载完成',
                                   wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                os.startfile(result[1])
        else:
            self.status_bar.SetStatusText('', 1)
            wx.MessageBox(result[1])

    def show_exception(self, exception):
        if exception[0] == 'DatabaseError':
            self.status_bar.SetStatusText('数据库错误，请重连', 1)
        wx.MessageBox('%s: %s' % exception)

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
        self.top_trans_text.SetLabel(s_date + self.org_nick_name + '  总金额：' + str(self.total_amt) + '元')
        self.SetCursor(wx.Cursor(wx.CURSOR_WAIT))
        self.reset_status()
        self.status = self.get_and_show_status()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))

    def on_ca_button(self, event):
        """
        用户点击对账按钮
        :param event:
        :return:
        """
        md = wx.MessageDialog(None, '确定进行对账？', 'B2301对账', wx.YES_NO | wx.ICON_QUESTION)
        if md.ShowModal() == wx.ID_YES:
            re_check = self.fb.post_check_account(self.tran_date, self.settle_type, self.org_nick_name)
            md.Destroy()
            if re_check:  # 已经对过账，不能重复对账
                wx.MessageBox('不能重复对账！')
            self.get_and_show_status()
            self.ca_button.Disable()
        else:
            md.Destroy()

    def on_ca_detail(self, event):
        if not self.btn_code_dict['ca_button']:
            return
        elif self.btn_code_dict['ca_button'] == -1:
            if self.status.get('unchecked'):
                msg = '未对账金额多了： %.2f' % (float(self.status['unchecked'][0][0]) - self.total_amt)
                wx.MessageBox(msg)
            elif self.status.get('checked'):
                msg = '对账金额多了： %.2f' % (float(self.status['checked'][0][0]) - self.total_amt)
                wx.MessageBox(msg)
            else:
                wx.MessageBox('未知错误！')
        elif self.btn_code_dict['ca_button'] == -2:
            ad = FesAae076Dialog(self, self.fb, self.tran_date, self.settle_type,
                                 self.org_nick_name, self.status['repeat_aae076'])
            if ad.ShowModal() == wx.ID_CANCEL:
                ad.Destroy()

    def on_cs_button(self, event):
        """
        用户点击清算按钮
        :param event:
        :return:
        """
        md = wx.MessageDialog(None, '确定进行清算？', 'B2304清算', wx.YES_NO | wx.ICON_QUESTION)
        if md.ShowModal() == wx.ID_YES:
            md.Destroy()
            re_settle = self.fb.post_check_settle(self.tran_date, self.settle_type, self.org_nick_name)
            if re_settle:  # 已经清算过，不能重复清算
                wx.MessageBox('不能重复清算！')
            self.get_and_show_status()
            self.cs_button.Disable()
        else:
            md.Destroy()

    def on_cs_detail(self, event):
        if self.btn_code_dict['cs_button'] == -1:
            if self.status.get('settled'):
                msg = '清算金额多了： %.2f' % (self.get_total_amt(self.status.get('settled')) - self.total_amt)
                wx.MessageBox(msg)
            else:
                wx.MessageBox('未知错误！')

    def on_cc_button(self, event):
        md = wx.MessageDialog(None, '确定发送B2211回写请求？', 'B2211', wx.YES_NO | wx.ICON_QUESTION)
        if md.ShowModal() == wx.ID_YES:
            self.fb.post_b2211()
        md.Destroy()

    def on_cc_detail(self, event):
        if self.btn_code_dict['cc_button'] == -1:
            if self.status.get('confirmed'):
                msg = '到账金额多了： %.2f' % (self.get_total_amt(self.status.get('confirmed')) - self.total_amt)
                wx.MessageBox(msg)
            else:
                wx.MessageBox('未知错误！')

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

        for k in self.btn_code_dict.keys():
            self.btn_code_dict[k] = 0

    def get_and_show_status(self):
        """
        获取并显示当日当前业务的对账清算到账状态
        :return:
        """
        status_dict = self.fb.check_status(self.tran_date, self.settle_type, self.org_nick_name)
        logger.debug('[%s][%s]: %s' % (self.tran_date, self.org_nick_name, status_dict))
        if status_dict.get('no_business'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('无业务')
            self.ca_static_text.SetForegroundColour(self.rgb_dict['Black'])
        elif status_dict.get('unchecked'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('未对账')
            if status_dict.get('repeat_aae076'):
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.SetLabel('对账文件笔数和\n更新笔数不一致!')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
                self.btn_code_dict['ca_button'] = -2
            elif abs(self.get_total_amt(status_dict.get('unchecked')) - self.total_amt) < 0.001:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Blue'])
            else:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.SetLabel('金额不一致!')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
                self.btn_code_dict['ca_button'] = -1
            self.ca_button.Enable()
            insert_into_gird(self.ca_grid, status_dict.get('unchecked'))
        elif status_dict.get('checked'):
            self.ca_static_text.Enable()
            self.ca_static_text.SetLabel('已对账')
            if status_dict.get('check_diff'):
                self.ca_detail_text.SetLabel('存在单边账!')
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Red'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
            elif abs(self.get_total_amt(status_dict.get('checked')) - self.total_amt) < 0.001:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['LimeGreen'])
            else:
                self.ca_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.SetLabel('对账金额与总\n金额不一致！')
                self.ca_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.ca_detail_text.Show()
                self.ca_detail_button.Show()
                self.btn_code_dict['ca_button'] = -1
            insert_into_gird(self.ca_grid, status_dict.get('checked'))

        if status_dict.get('unsettled'):
            self.cs_static_text.Enable()
            self.cs_static_text.SetLabel('未清算')
            self.cs_static_text.SetForegroundColour(self.rgb_dict['Blue'])
            self.cs_button.Enable()
        elif status_dict.get('settled'):
            self.cs_static_text.Enable()
            self.cs_static_text.SetLabel('已清算')
            if abs(self.get_total_amt(status_dict.get('settled')) - self.total_amt) < 0.001:
                self.cs_static_text.SetForegroundColour(self.rgb_dict['LimeGreen'])
            else:
                self.cs_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.cs_detail_text.SetLabel('清算金额与总\n金额不一致！')
                self.cs_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.cs_detail_text.Show()
                self.cs_detail_button.Show()
                self.btn_code_dict['cs_button'] = -1
            insert_into_gird(self.cs_grid, status_dict.get('settled'))

        if status_dict.get('unconfirmed'):
            self.cc_static_text.Enable()
            self.cc_static_text.SetLabel('未到账')
            self.cc_static_text.SetForegroundColour(self.rgb_dict['Blue'])
        elif status_dict.get('confirmed'):
            self.cc_static_text.Enable()
            self.cc_detail_text.Show()
            self.cc_detail_button.Show()
            flag_03 = False
            flag_11 = False
            flag_success = True
            for row in status_dict.get('confirmed'):
                if '03' == row[1]:
                    flag_03 = True
                if '11' == row[1]:
                    flag_11 = True
                if '12' != row[1]:
                    flag_success = False
            if flag_03:
                self.cc_static_text.SetLabel('未转账')
                self.cc_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.cc_detail_text.SetLabel('已生成流水')
                self.cc_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
            elif flag_11:
                self.cc_static_text.SetLabel('未到账')
                self.cc_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                self.cc_detail_text.SetLabel('未确认到账')
                self.cc_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
            elif flag_success:
                self.cc_static_text.SetLabel('已到账')
                if abs(self.get_total_amt(status_dict.get('confirmed')) - self.total_amt) < 0.001:
                    self.cc_static_text.SetForegroundColour(self.rgb_dict['LimeGreen'])
                    self.cc_button.Enable()
                    self.cc_detail_text.Hide()
                    self.cc_detail_button.Hide()
                else:
                    self.cc_static_text.SetForegroundColour(self.rgb_dict['Gold'])
                    self.cc_detail_text.SetLabel('到账金额与总\n金额不一致！')
                    self.cc_detail_text.SetForegroundColour(self.rgb_dict['Gold'])
                    self.btn_code_dict['cc_button'] = -1
            else:
                self.cc_static_text.SetLabel('未到账')
                self.cc_static_text.SetForegroundColour(self.rgb_dict['Red'])
                self.cc_detail_text.SetLabel('未知异常！')
                self.cc_detail_text.SetForegroundColour(self.rgb_dict['Red'])
            insert_into_gird(self.cc_grid, status_dict.get('confirmed'))
        self.Layout()
        return status_dict

    def on_mib9999(self, event):
        dlg = FesB9999Dialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            self.status_bar.SetStatusText('正在后台下载过渡户交易明细文件...', 1)
            ba, sd, ed = dlg.get_selection()
            B9999Thread(ba, sd, ed)
        dlg.Destroy()

    def on_mib2306(self, event):
        md = wx.MessageDialog(None, '确定发送B2306请求生成退款文件？', 'B2306', wx.YES_NO | wx.ICON_QUESTION)
        if md.ShowModal() == wx.ID_YES:
            self.fb.post_b2306()
        md.Destroy()

    def delete_check_info(self, event):
        """
        删除某日期的对账信息
        :param event:
        :return:
        """
        dlg = FesDelChkDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            print('功能未实现。。。')
        dlg.Destroy()

    def on_get_daily(self, event):
        event.Skip()

    def on_open_log(self, event):
        log_file = ('%s/logs/%s_fes_assist_log.txt' %
                    (os.getcwd(), datetime.date.today().strftime('%Y%m%d'))).replace('\\', '/')
        if os.path.exists(log_file):
            os.startfile(log_file)
        else:
            wx.MessageBox('打开失败，找不到文件：%s' % log_file)

    def on_open_log_dir(self, event):
        log_dir = "%s\\logs" % os.getcwd()
        if os.path.exists(log_dir):
            os.system('start explorer ' + log_dir)
        else:
            wx.MessageBox('打开失败，找不到文件夹：%s' % log_dir)

    def on_reconnect(self, event):
        if self.fb.reconnect():
            self.status_bar.SetStatusText('', 1)
            wx.MessageBox('连接数据库成功')
        else:
            wx.MessageBox('连接失败！')

    @staticmethod
    def get_total_amt(data):
        if not len(data):
            return 0
        total = 0.0
        for row in data:
            total += float(row[0])
        return total
