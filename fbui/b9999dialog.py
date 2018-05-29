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

        bank_choiceChoices = [u"工商银行代收：3002010011200508811", u"工商银行代发：3002010011920101028",
                              u"建设银行代收：65001610200052513865", u"建设银行代发：65001610200052513858"]
        self.bank_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bank_choiceChoices, 0)
        self.bank_choice.SetSelection(1)
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


