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

    def on_open_log(self, event):
        event.Skip()

    def on_open_log_dir(self, event):
        event.Skip()

    def on_reconnect(self, event):
        event.Skip()


###########################################################################
## Class Aae076Dialog
###########################################################################

class Aae076Dialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"对账文件笔数和更新笔数不一致!", pos=wx.DefaultPosition,
                           size=wx.Size(750, 450), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)

        ad_sizer = wx.BoxSizer(wx.VERTICAL)

        self.info_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.info_panel.SetMaxSize(wx.Size(-1, 60))

        info_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.info_text = wx.StaticText(self.info_panel, wx.ID_ANY, u"info", wx.DefaultPosition, wx.DefaultSize, 0)
        self.info_text.Wrap(-1)
        self.info_text.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))
        self.info_text.SetForegroundColour(wx.Colour(255, 0, 0))

        info_sizer.Add(self.info_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.refresh_button = wx.Button(self.info_panel, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        info_sizer.Add(self.refresh_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.info_panel.SetSizer(info_sizer)
        self.info_panel.Layout()
        info_sizer.Fit(self.info_panel)
        ad_sizer.Add(self.info_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.gird_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gird_sizer = wx.StaticBoxSizer(wx.StaticBox(self.gird_panel, wx.ID_ANY, u"详情"), wx.VERTICAL)

        self.aae076_text = wx.StaticText(gird_sizer.GetStaticBox(), wx.ID_ANY, u"双击行号查看详情", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.aae076_text.Wrap(-1)
        gird_sizer.Add(self.aae076_text, 0, wx.ALL, 5)

        self.aae076_grid = wx.grid.Grid(gird_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.aae076_grid.CreateGrid(1, 3)
        self.aae076_grid.EnableEditing(True)
        self.aae076_grid.EnableGridLines(True)
        self.aae076_grid.EnableDragGridSize(False)
        self.aae076_grid.SetMargins(0, 0)

        # Columns
        self.aae076_grid.EnableDragColMove(False)
        self.aae076_grid.EnableDragColSize(True)
        self.aae076_grid.SetColLabelSize(30)
        self.aae076_grid.SetColLabelValue(0, u"ORG_NICK_NAME")
        self.aae076_grid.SetColLabelValue(1, u"AAE076")
        self.aae076_grid.SetColLabelValue(2, u"COUNT")
        self.aae076_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.aae076_grid.EnableDragRowSize(True)
        self.aae076_grid.SetRowLabelSize(80)
        self.aae076_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.aae076_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gird_sizer.Add(self.aae076_grid, 0, wx.ALL, 5)

        self.detail_text = wx.StaticText(gird_sizer.GetStaticBox(), wx.ID_ANY, u"双击行号删除记录", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.detail_text.Wrap(-1)
        gird_sizer.Add(self.detail_text, 0, wx.ALL, 5)

        self.detail_grid = wx.grid.Grid(gird_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.detail_grid.CreateGrid(1, 5)
        self.detail_grid.EnableEditing(True)
        self.detail_grid.EnableGridLines(True)
        self.detail_grid.EnableDragGridSize(False)
        self.detail_grid.SetMargins(0, 0)

        # Columns
        self.detail_grid.EnableDragColMove(False)
        self.detail_grid.EnableDragColSize(True)
        self.detail_grid.SetColLabelSize(30)
        self.detail_grid.SetColLabelValue(0, u"AAE076")
        self.detail_grid.SetColLabelValue(1, u"TRANS_STATUS")
        self.detail_grid.SetColLabelValue(2, u"FUND_STATUS")
        self.detail_grid.SetColLabelValue(3, u"ID")
        self.detail_grid.SetColLabelValue(4, u"TOTAL_AMT")
        self.detail_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.detail_grid.EnableDragRowSize(True)
        self.detail_grid.SetRowLabelSize(80)
        self.detail_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.detail_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gird_sizer.Add(self.detail_grid, 0, wx.ALL, 5)

        self.gird_panel.SetSizer(gird_sizer)
        self.gird_panel.Layout()
        gird_sizer.Fit(self.gird_panel)
        ad_sizer.Add(self.gird_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(ad_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.refresh_button.Bind(wx.EVT_BUTTON, self.on_get_repeat_aae076)
        self.aae076_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.on_show_details)
        self.detail_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.on_delete_row)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_get_repeat_aae076(self, event):
        event.Skip()

    def on_show_details(self, event):
        event.Skip()

    def on_delete_row(self, event):
        event.Skip()


###########################################################################
## Class DelChkDialog
###########################################################################

class DelChkDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"删除对账信息", pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        del_sizer = wx.BoxSizer(wx.VERTICAL)

        self.warning_text = wx.StaticText(self, wx.ID_ANY, u"删除某日的对账信息，以便进行重新对账，请谨慎操作！", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.warning_text.Wrap(-1)
        self.warning_text.SetFont(
            wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "宋体"))
        self.warning_text.SetForegroundColour(wx.Colour(255, 0, 0))

        del_sizer.Add(self.warning_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.choose_text = wx.StaticText(self, wx.ID_ANY, u"选择要删除的日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.choose_text.Wrap(-1)
        p_sizer.Add(self.choose_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                 wx.DefaultSize, wx.adv.DP_DROPDOWN)
        p_sizer.Add(self.date_picker, 0, wx.ALL, 5)

        del_sizer.Add(p_sizer, 1, wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        b_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.ok_button = wx.Button(self, wx.ID_OK, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        b_sizer.Add(self.ok_button, 0, wx.ALL, 5)

        self.cancel_button = wx.Button(self, wx.ID_CANCEL, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        b_sizer.Add(self.cancel_button, 0, wx.ALL, 5)

        del_sizer.Add(b_sizer, 1, wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        self.SetSizer(del_sizer)
        self.Layout()
        del_sizer.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_ok(self, event):
        event.Skip()

    def on_cancel(self, event):
        event.Skip()


###########################################################################
## Class B9999Dialog
###########################################################################

class B9999Dialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"下载过渡户交易明细文件(发送B9999请求)：", pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        bank_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.bank_text = wx.StaticText(self, wx.ID_ANY, u"选择银行过渡户:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bank_text.Wrap(-1)
        bank_sizer.Add(self.bank_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bank_choiceChoices = []
        self.bank_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bank_choiceChoices, 0)
        self.bank_choice.SetSelection(0)
        self.bank_choice.SetMinSize(wx.Size(280, -1))

        bank_sizer.Add(self.bank_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        main_sizer.Add(bank_sizer, 1, wx.EXPAND, 5)

        sd_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sd_text = wx.StaticText(self, wx.ID_ANY, u"选择开始日期： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.sd_text.Wrap(-1)
        sd_sizer.Add(self.sd_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.sd_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.adv.DP_DROPDOWN)
        sd_sizer.Add(self.sd_date_picker, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        main_sizer.Add(sd_sizer, 1, wx.EXPAND, 5)

        ed_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.ed_text = wx.StaticText(self, wx.ID_ANY, u"选择结束日期： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ed_text.Wrap(-1)
        ed_sizer.Add(self.ed_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ed_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.adv.DP_DROPDOWN)
        ed_sizer.Add(self.ed_date_picker, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        main_sizer.Add(ed_sizer, 1, wx.EXPAND, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        bi_sizer = wx.GridSizer(1, 2, 0, 0)

        self.btn_ok = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bi_sizer.Add(self.btn_ok, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btn_cancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bi_sizer.Add(self.btn_cancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        btn_sizer.Add(bi_sizer, 1, wx.ALIGN_CENTER | wx.EXPAND, 5)

        main_sizer.Add(btn_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(main_sizer)
        self.Layout()
        main_sizer.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_ok(self, event):
        event.Skip()

    def on_cancel(self, event):
        event.Skip()


###########################################################################
## Class DailyDialog
###########################################################################

class DailyDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"生成日报文件", pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        daily_sizer = wx.BoxSizer(wx.VERTICAL)

        self.title_text = wx.StaticText(self, wx.ID_ANY, u"三版FES运营日报", wx.DefaultPosition, wx.DefaultSize, 0)
        self.title_text.Wrap(-1)
        daily_sizer.Add(self.title_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        r_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.report_d_text = wx.StaticText(self, wx.ID_ANY, u"填报日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.report_d_text.Wrap(-1)
        r_sizer.Add(self.report_d_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rd_date_picker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.adv.DP_DEFAULT)
        r_sizer.Add(self.rd_date_picker, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.report_p_text = wx.StaticText(self, wx.ID_ANY, u"填报人", wx.DefaultPosition, wx.DefaultSize, 0)
        self.report_p_text.Wrap(-1)
        r_sizer.Add(self.report_p_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rp_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, u"杨飞", wx.DefaultPosition, wx.DefaultSize, 0)
        r_sizer.Add(self.rp_text_ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        daily_sizer.Add(r_sizer, 1, wx.EXPAND, 5)

        self.o_text = wx.StaticText(self, wx.ID_ANY, u"联机业务起止日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.o_text.Wrap(-1)
        daily_sizer.Add(self.o_text, 0, wx.ALL, 5)

        o_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.start_text = wx.StaticText(self, wx.ID_ANY, u"开始日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.start_text.Wrap(-1)
        o_sizer.Add(self.start_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_datePicker6 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize, wx.adv.DP_DEFAULT)
        o_sizer.Add(self.m_datePicker6, 0, wx.ALL, 5)

        self.end_text = wx.StaticText(self, wx.ID_ANY, u"结束日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.end_text.Wrap(-1)
        o_sizer.Add(self.end_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_datePicker7 = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                                   wx.DefaultSize, wx.adv.DP_DEFAULT)
        o_sizer.Add(self.m_datePicker7, 0, wx.ALL, 5)

        daily_sizer.Add(o_sizer, 1, wx.EXPAND, 5)

        self.ok_btn = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        daily_sizer.Add(self.ok_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(daily_sizer)
        self.Layout()
        daily_sizer.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.ok_btn.Bind(wx.EVT_BUTTON, self.on_ok)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_ok(self, event):
        event.Skip()


