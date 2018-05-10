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
                          size=wx.Size(1000, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        root_sizer = wx.BoxSizer(wx.VERTICAL)

        self.root_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER | wx.TAB_TRAVERSAL)
        inner_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_trans_text = wx.StaticText(self.root_panel, wx.ID_ANY, u"fes", wx.DefaultPosition, wx.DefaultSize, 0)
        self.top_trans_text.Wrap(-1)
        self.top_trans_text.SetFont(
            wx.Font(15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑"))

        inner_sizer.Add(self.top_trans_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        config_sizer = wx.StaticBoxSizer(wx.StaticBox(self.root_panel, wx.ID_ANY, u"设置"), wx.HORIZONTAL)

        self.trans_choice_text = wx.StaticText(config_sizer.GetStaticBox(), wx.ID_ANY, u"选择交易类型：", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.trans_choice_text.Wrap(-1)
        config_sizer.Add(self.trans_choice_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        trans_choiceChoices = [u"未选择", u"工商银行大厅POS", u"工商银行一体机IMAC", u"工商银行APP", u"招商银行大厅POS", u"建设银行APP"]
        self.trans_choice = wx.Choice(config_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      trans_choiceChoices, 0)
        self.trans_choice.SetSelection(0)
        config_sizer.Add(self.trans_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_date_text = wx.StaticText(config_sizer.GetStaticBox(), wx.ID_ANY, u"          选择交易日期：",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.trans_date_text.Wrap(-1)
        config_sizer.Add(self.trans_date_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.trans_date_picker = wx.adv.DatePickerCtrl(config_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                       wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT)
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

        inner_sizer.Add(config_sizer, 1, wx.ALL | wx.EXPAND, 10)

        status_sizer = wx.StaticBoxSizer(wx.StaticBox(self.root_panel, wx.ID_ANY, u"状态"), wx.VERTICAL)

        ca_sizer = wx.WrapSizer(wx.HORIZONTAL)

        self.ca_static_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, u"未对账", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.ca_static_text.Wrap(-1)
        self.ca_static_text.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑"))

        ca_sizer.Add(self.ca_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ca_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"对账", wx.DefaultPosition, wx.DefaultSize, 0)
        ca_sizer.Add(self.ca_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        status_sizer.Add(ca_sizer, 1, wx.EXPAND, 5)

        self.ca_static_line = wx.StaticLine(status_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        status_sizer.Add(self.ca_static_line, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        cs_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.cs_static_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, u"未清算", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cs_static_text.Wrap(-1)
        self.cs_static_text.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑"))

        cs_sizer.Add(self.cs_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cs_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"清算", wx.DefaultPosition, wx.DefaultSize, 0)
        cs_sizer.Add(self.cs_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        status_sizer.Add(cs_sizer, 1, wx.EXPAND, 5)

        self.cs_static_line = wx.StaticLine(status_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        status_sizer.Add(self.cs_static_line, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        cc_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.cc_static_text = wx.StaticText(status_sizer.GetStaticBox(), wx.ID_ANY, u"未到账", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.cc_static_text.Wrap(-1)
        self.cc_static_text.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑"))

        cc_sizer.Add(self.cc_static_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cc_button = wx.Button(status_sizer.GetStaticBox(), wx.ID_ANY, u"回写", wx.DefaultPosition, wx.DefaultSize, 0)
        cc_sizer.Add(self.cc_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        status_sizer.Add(cc_sizer, 1, wx.EXPAND, 5)

        inner_sizer.Add(status_sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.root_panel.SetSizer(inner_sizer)
        self.root_panel.Layout()
        inner_sizer.Fit(self.root_panel)
        root_sizer.Add(self.root_panel, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(root_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.trans_choice.Bind(wx.EVT_CHOICE, self.on_choose_tran_type)
        self.trans_date_picker.Bind(wx.adv.EVT_DATE_CHANGED, self.on_change_date)
        self.status_button.Bind(wx.EVT_BUTTON, self.on_get_status)
        self.ca_button.Bind(wx.EVT_BUTTON, self.on_ca_button)
        self.cs_button.Bind(wx.EVT_BUTTON, self.on_cs_button)
        self.cc_button.Bind(wx.EVT_BUTTON, self.on_cc_button)

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

    def on_cs_button(self, event):
        event.Skip()

    def on_cc_button(self, event):
        event.Skip()


