# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid


###########################################################################
## Class RootFrame
###########################################################################

class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"FES ASSIST", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        root_sizer = wx.BoxSizer(wx.VERTICAL)

        self.root_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER | wx.TAB_TRAVERSAL)
        inner_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_trans_text = wx.StaticText(self.root_panel, wx.ID_ANY, u"FES", wx.DefaultPosition, wx.DefaultSize, 0)
        self.top_trans_text.Wrap(-1)
        self.top_trans_text.SetFont(
            wx.Font(15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑"))

        inner_sizer.Add(self.top_trans_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.config_panel = wx.Panel(self.root_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.config_panel.SetMaxSize(wx.Size(-1, 100))

        config_sizer = wx.StaticBoxSizer(wx.StaticBox(self.config_panel, wx.ID_ANY, u"设置"), wx.HORIZONTAL)

        self.trans_choice_text = wx.StaticText(config_sizer.GetStaticBox(), wx.ID_ANY, u"选择交易类型：", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.trans_choice_text.Wrap(-1)
        config_sizer.Add(self.trans_choice_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        trans_choiceChoices = [u"未选择", u"工商银行大厅POS", u"工商银行一体机IMAC", u"工商银行APP", u"招商银行大厅POS", u"建设银行大厅POS", u"建设银行APP"]
        self.trans_choice = wx.Choice(config_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      trans_choiceChoices, 0)
        self.trans_choice.SetSelection(0)
        config_sizer.Add(self.trans_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_date_text = wx.StaticText(config_sizer.GetStaticBox(), wx.ID_ANY, u"          选择交易日期：",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.trans_date_text.Wrap(-1)
        config_sizer.Add(self.trans_date_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_date_picker = wx.adv.DatePickerCtrl(config_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                       wx.DefaultPosition, wx.Size(-1, -1), wx.adv.DP_DROPDOWN)
        config_sizer.Add(self.trans_date_picker, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_amt_text = wx.StaticText(config_sizer.GetStaticBox(), wx.ID_ANY, u"          总金额：",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.trans_amt_text.Wrap(-1)
        config_sizer.Add(self.trans_amt_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.amt_text_ctrl = wx.TextCtrl(config_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(150, -1), 0)
        self.amt_text_ctrl.SetMaxLength(20)
        config_sizer.Add(self.amt_text_ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.blank_static_text = wx.StaticText(config_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.blank_static_text.Wrap(-1)
        config_sizer.Add(self.blank_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.status_button = wx.Button(config_sizer.GetStaticBox(), wx.ID_ANY, u"查询状态", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        config_sizer.Add(self.status_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.config_panel.SetSizer(config_sizer)
        self.config_panel.Layout()
        config_sizer.Fit(self.config_panel)
        inner_sizer.Add(self.config_panel, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.status_panel = wx.Panel(self.root_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        status_sizer = wx.StaticBoxSizer(wx.StaticBox(self.status_panel, wx.ID_ANY, u"状态"), wx.VERTICAL)

        ca_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.ca_static_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, u"未对账", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.ca_static_text.Wrap(-1)
        self.ca_static_text.SetFont(
            wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))

        ca_sizer.Add(self.ca_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ca_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"对账", wx.DefaultPosition, wx.DefaultSize, 0)
        ca_sizer.Add(self.ca_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ca_grid = wx.grid.Grid(status_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.ca_grid.CreateGrid(1, 2)
        self.ca_grid.EnableEditing(True)
        self.ca_grid.EnableGridLines(True)
        self.ca_grid.EnableDragGridSize(False)
        self.ca_grid.SetMargins(0, 0)

        # Columns
        self.ca_grid.EnableDragColMove(False)
        self.ca_grid.EnableDragColSize(True)
        self.ca_grid.SetColLabelSize(30)
        self.ca_grid.SetColLabelValue(0, u"金额")
        self.ca_grid.SetColLabelValue(1, u"笔数")
        self.ca_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.ca_grid.EnableDragRowSize(True)
        self.ca_grid.SetRowLabelSize(80)
        self.ca_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.ca_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        ca_sizer.Add(self.ca_grid, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ca_detail_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.ca_detail_text.Wrap(-1)
        ca_sizer.Add(self.ca_detail_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ca_detail_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"查看详情", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        ca_sizer.Add(self.ca_detail_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        status_sizer.Add(ca_sizer, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        cs_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.cs_static_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, u"未清算", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cs_static_text.Wrap(-1)
        self.cs_static_text.SetFont(
            wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))

        cs_sizer.Add(self.cs_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cs_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"清算", wx.DefaultPosition, wx.DefaultSize, 0)
        cs_sizer.Add(self.cs_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cs_grid = wx.grid.Grid(status_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.cs_grid.CreateGrid(1, 4)
        self.cs_grid.EnableEditing(True)
        self.cs_grid.EnableGridLines(True)
        self.cs_grid.EnableDragGridSize(False)
        self.cs_grid.SetMargins(0, 0)

        # Columns
        self.cs_grid.EnableDragColMove(False)
        self.cs_grid.EnableDragColSize(True)
        self.cs_grid.SetColLabelSize(30)
        self.cs_grid.SetColLabelValue(0, u"SETTLE_AMT")
        self.cs_grid.SetColLabelValue(1, u"IS_CONFIRMED")
        self.cs_grid.SetColLabelValue(2, u"SETTLE_STATUS")
        self.cs_grid.SetColLabelValue(3, u"CURRENT_DIRECTION")
        self.cs_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.cs_grid.EnableDragRowSize(True)
        self.cs_grid.SetRowLabelSize(80)
        self.cs_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.cs_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        cs_sizer.Add(self.cs_grid, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cs_detail_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cs_detail_text.Wrap(-1)
        cs_sizer.Add(self.cs_detail_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cs_detail_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"查看详情", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        cs_sizer.Add(self.cs_detail_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        status_sizer.Add(cs_sizer, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        cc_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.cc_static_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, u"未到账", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cc_static_text.Wrap(-1)
        self.cc_static_text.SetFont(
            wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))

        cc_sizer.Add(self.cc_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cc_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"回写", wx.DefaultPosition, wx.DefaultSize, 0)
        cc_sizer.Add(self.cc_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cc_grid = wx.grid.Grid(status_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.cc_grid.CreateGrid(1, 4)
        self.cc_grid.EnableEditing(True)
        self.cc_grid.EnableGridLines(True)
        self.cc_grid.EnableDragGridSize(False)
        self.cc_grid.SetMargins(0, 0)

        # Columns
        self.cc_grid.EnableDragColMove(False)
        self.cc_grid.EnableDragColSize(True)
        self.cc_grid.SetColLabelSize(30)
        self.cc_grid.SetColLabelValue(0, u"TRAN_AMT")
        self.cc_grid.SetColLabelValue(1, u"STATUS")
        self.cc_grid.SetColLabelValue(2, u"IS_CHECK")
        self.cc_grid.SetColLabelValue(3, u"CURRENT_DIRECTION")
        self.cc_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.cc_grid.EnableDragRowSize(True)
        self.cc_grid.SetRowLabelSize(80)
        self.cc_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.cc_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        cc_sizer.Add(self.cc_grid, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cc_detail_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cc_detail_text.Wrap(-1)
        cc_sizer.Add(self.cc_detail_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cc_detail_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"查看详情", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        cc_sizer.Add(self.cc_detail_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        status_sizer.Add(cc_sizer, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.status_panel.SetSizer(status_sizer)
        self.status_panel.Layout()
        status_sizer.Fit(self.status_panel)
        inner_sizer.Add(self.status_panel, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.root_panel.SetSizer(inner_sizer)
        self.root_panel.Layout()
        inner_sizer.Fit(self.root_panel)
        root_sizer.Add(self.root_panel, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(root_sizer)
        self.Layout()
        self.menu_bar = wx.MenuBar(0)
        self.menu_req = wx.Menu()
        self.mi_b9999 = wx.MenuItem(self.menu_req, wx.ID_ANY, u"获取过渡户交易明细...", u"发送B9999请求下载过渡户交易明细文件", wx.ITEM_NORMAL)
        self.menu_req.Append(self.mi_b9999)

        self.mi_b2306 = wx.MenuItem(self.menu_req, wx.ID_ANY, u"B2306 生成退款文件", u"发送B2306请求生成联机业务的退款文件", wx.ITEM_NORMAL)
        self.menu_req.Append(self.mi_b2306)

        self.mi_b2211 = wx.MenuItem(self.menu_req, wx.ID_ANY, u"B2211 联机业务回写", u"发送B2211请求将三版联机业务回写给业务系统",
                                    wx.ITEM_NORMAL)
        self.menu_req.Append(self.mi_b2211)

        self.menu_bar.Append(self.menu_req, u"请求")

        self.menu_settle = wx.Menu()
        self.mi_rw = wx.MenuItem(self.menu_settle, wx.ID_ANY, u"行内转账流水生成", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_settle.Append(self.mi_rw)

        self.mi_transfer = wx.MenuItem(self.menu_settle, wx.ID_ANY, u"转账", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_settle.Append(self.mi_transfer)

        self.mi_confirm = wx.MenuItem(self.menu_settle, wx.ID_ANY, u"确认到账", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_settle.Append(self.mi_confirm)

        self.menu_bar.Append(self.menu_settle, u"清算")

        self.menu_opa = wx.Menu()
        self.mi_re_check = wx.MenuItem(self.menu_opa, wx.ID_ANY, u"删除对账信息...", u"删除某日期的已对账信息，以便进行该日的重新对账，请谨慎操作！",
                                       wx.ITEM_NORMAL)
        self.menu_opa.Append(self.mi_re_check)

        self.mi_daily = wx.MenuItem(self.menu_opa, wx.ID_ANY, u"生成日报...", u"生成指定日期的日报文件", wx.ITEM_NORMAL)
        self.menu_opa.Append(self.mi_daily)

        self.mi_time = wx.MenuItem(self.menu_opa, wx.ID_ANY, u"修改远程服务器时间...", u"查看并修改远端服务器主机的时间", wx.ITEM_NORMAL)
        self.menu_opa.Append(self.mi_time)

        self.menu_bar.Append(self.menu_opa, u"操作")

        self.menu_help = wx.Menu()
        self.mi_open_log = wx.MenuItem(self.menu_help, wx.ID_ANY, u"查看日志", u"打开当前使用的日志文件", wx.ITEM_NORMAL)
        self.menu_help.Append(self.mi_open_log)

        self.mi_log_dir = wx.MenuItem(self.menu_help, wx.ID_ANY, u"打开日志文件夹", u"打开存放日志的文件夹", wx.ITEM_NORMAL)
        self.menu_help.Append(self.mi_log_dir)

        self.mi_reconnect = wx.MenuItem(self.menu_help, wx.ID_ANY, u"连接数据库", u"重新建立数据库连接", wx.ITEM_NORMAL)
        self.menu_help.Append(self.mi_reconnect)

        self.menu_bar.Append(self.menu_help, u"帮助")

        self.SetMenuBar(self.menu_bar)

        self.status_bar = self.CreateStatusBar(2, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.trans_choice.Bind(wx.EVT_CHOICE, self.on_choose_tran_type)
        self.trans_date_picker.Bind(wx.adv.EVT_DATE_CHANGED, self.on_change_date)
        self.status_button.Bind(wx.EVT_BUTTON, self.on_get_status)
        self.ca_button.Bind(wx.EVT_BUTTON, self.on_ca_button)
        self.ca_detail_button.Bind(wx.EVT_BUTTON, self.on_ca_detail)
        self.cs_button.Bind(wx.EVT_BUTTON, self.on_cs_button)
        self.cs_detail_button.Bind(wx.EVT_BUTTON, self.on_cs_detail)
        self.cc_button.Bind(wx.EVT_BUTTON, self.on_cc_button)
        self.cc_detail_button.Bind(wx.EVT_BUTTON, self.on_cc_detail)
        self.Bind(wx.EVT_MENU, self.on_mib9999, id=self.mi_b9999.GetId())
        self.Bind(wx.EVT_MENU, self.on_mib2306, id=self.mi_b2306.GetId())
        self.Bind(wx.EVT_MENU, self.on_cc_button, id=self.mi_b2211.GetId())
        self.Bind(wx.EVT_MENU, self.delete_check_info, id=self.mi_re_check.GetId())
        self.Bind(wx.EVT_MENU, self.on_get_daily, id=self.mi_daily.GetId())
        self.Bind(wx.EVT_MENU, self.on_show_time_dialog, id=self.mi_time.GetId())
        self.Bind(wx.EVT_MENU, self.on_open_log, id=self.mi_open_log.GetId())
        self.Bind(wx.EVT_MENU, self.on_open_log_dir, id=self.mi_log_dir.GetId())
        self.Bind(wx.EVT_MENU, self.on_reconnect, id=self.mi_reconnect.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_choose_tran_type(self, event):
        event.Skip()

    def on_change_date(self, event):
        event.Skip()

    def on_get_status(self, event):
        event.Skip()

    def on_ca_button(self, event):
        event.Skip()

    def on_ca_detail(self, event):
        event.Skip()

    def on_cs_button(self, event):
        event.Skip()

    def on_cs_detail(self, event):
        event.Skip()

    def on_cc_button(self, event):
        event.Skip()

    def on_cc_detail(self, event):
        event.Skip()

    def on_mib9999(self, event):
        event.Skip()

    def on_mib2306(self, event):
        event.Skip()

    def delete_check_info(self, event):
        event.Skip()

    def on_get_daily(self, event):
        event.Skip()

    def on_show_time_dialog(self, event):
        event.Skip()

    def on_open_log(self, event):
        event.Skip()

    def on_open_log_dir(self, event):
        event.Skip()

    def on_reconnect(self, event):
        event.Skip()


