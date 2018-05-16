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


