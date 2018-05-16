# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


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
        self.aae076_grid.CreateGrid(1, 5)
        self.aae076_grid.EnableEditing(True)
        self.aae076_grid.EnableGridLines(True)
        self.aae076_grid.EnableDragGridSize(False)
        self.aae076_grid.SetMargins(0, 0)

        # Columns
        self.aae076_grid.EnableDragColMove(False)
        self.aae076_grid.EnableDragColSize(True)
        self.aae076_grid.SetColLabelSize(30)
        self.aae076_grid.SetColLabelValue(0, u"AAE076")
        self.aae076_grid.SetColLabelValue(1, u"TRANS_STATUS")
        self.aae076_grid.SetColLabelValue(2, u"FUND_STATUS")
        self.aae076_grid.SetColLabelValue(3, u"ID")
        self.aae076_grid.SetColLabelValue(4, u"TOTAL_AMT")
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


