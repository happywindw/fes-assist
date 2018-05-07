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

        self.root_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER | wx.TAB_TRAVERSAL)
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

        trans_choiceChoices = [u"未选择", u"工商银行大厅POS", u"工商银行一体机IMAC", u"工商银行APP", u"招商银行大厅POS", u"建设银行APP"]
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

        self.top_button = wx.Button(self.root_panel, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        top_sizer.Add(self.top_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        inner_sizer.Add(top_sizer, 1, wx.EXPAND, 5)

        status_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(self.root_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText4.Wrap(-1)
        status_sizer.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self.root_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)
        status_sizer.Add(self.m_staticText5, 0, wx.ALL, 5)

        inner_sizer.Add(status_sizer, 1, wx.EXPAND, 5)

        operate_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button2 = wx.Button(self.root_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        operate_sizer.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self.root_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        operate_sizer.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self.root_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        operate_sizer.Add(self.m_button4, 0, wx.ALL, 5)

        inner_sizer.Add(operate_sizer, 1, wx.EXPAND, 5)

        self.root_panel.SetSizer(inner_sizer)
        self.root_panel.Layout()
        inner_sizer.Fit(self.root_panel)
        root_sizer.Add(self.root_panel, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(root_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.trans_choice.Bind(wx.EVT_CHOICE, self.on_choose_tran_type)
        self.top_button.Bind(wx.EVT_BUTTON, self.on_top_button)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_choose_tran_type(self, event):
        event.Skip()

    def on_top_button(self, event):
        event.Skip()


