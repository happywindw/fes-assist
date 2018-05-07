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


###########################################################################
## Class RootFrame
###########################################################################

class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"FES ASSIST", pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        root_sizer = wx.BoxSizer(wx.VERTICAL)

        self.root_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        inner_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_static_text = wx.StaticText(self.root_panel, wx.ID_ANY, u"未选择交易类型", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.top_static_text.Wrap(-1)
        inner_sizer.Add(self.top_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.trans_choice_text = wx.StaticText(self.root_panel, wx.ID_ANY, u"选择交易类型：", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.trans_choice_text.Wrap(-1)
        top_sizer.Add(self.trans_choice_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        trans_choiceChoices = [u"工商银行大厅POS", u"工商银行一体机IMAC"]
        self.trans_choice = wx.Choice(self.root_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      trans_choiceChoices, 0)
        self.trans_choice.SetSelection(0)
        top_sizer.Add(self.trans_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_date_text = wx.StaticText(self.root_panel, wx.ID_ANY, u"选择交易日期：", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.trans_date_text.Wrap(-1)
        top_sizer.Add(self.trans_date_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_date_picker = wx.adv.DatePickerCtrl(self.root_panel, wx.ID_ANY, wx.DefaultDateTime,
                                                       wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT)
        top_sizer.Add(self.trans_date_picker, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        inner_sizer.Add(top_sizer, 1, wx.EXPAND, 5)

        self.top_panel = wx.Panel(self.root_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 100), wx.TAB_TRAVERSAL)
        inner_sizer.Add(self.top_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.root_panel.SetSizer(inner_sizer)
        self.root_panel.Layout()
        inner_sizer.Fit(self.root_panel)
        root_sizer.Add(self.root_panel, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(root_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


