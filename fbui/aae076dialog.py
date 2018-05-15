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
                           size=wx.Size(500, 300), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)

        ad_sizer = wx.BoxSizer(wx.VERTICAL)

        info_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.info_text = wx.StaticText(self, wx.ID_ANY, u"info", wx.DefaultPosition, wx.DefaultSize, 0)
        self.info_text.Wrap(-1)
        info_sizer.Add(self.info_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0)
        info_sizer.Add(self.m_button8, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ad_sizer.Add(info_sizer, 1, wx.EXPAND, 5)

        ag_sizer = wx.GridSizer(1, 1, 0, 0)

        self.aae076_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

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
        ag_sizer.Add(self.aae076_grid, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ad_sizer.Add(ag_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(ad_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


