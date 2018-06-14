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


