# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class TimeDialog
###########################################################################

class TimeDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"修改远程服务器时间", pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        time_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        time_sizer.SetFlexibleDirection(wx.BOTH)
        time_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.choose_text = wx.StaticText(self, wx.ID_ANY, u"选择远程服务器：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.choose_text.Wrap(-1)
        time_sizer.Add(self.choose_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        ser_choiceChoices = [wx.EmptyString, u"二版生产服务器"]
        self.ser_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ser_choiceChoices, 0)
        self.ser_choice.SetSelection(0)
        time_sizer.Add(self.ser_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.current_text = wx.StaticText(self, wx.ID_ANY, u"当前服务器时间：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.current_text.Wrap(-1)
        time_sizer.Add(self.current_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.time_text = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.time_text.Wrap(-1)
        time_sizer.Add(self.time_text, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.bk_text_01 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bk_text_01.Wrap(-1)
        time_sizer.Add(self.bk_text_01, 0, wx.ALL, 5)

        self.bk_text_02 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bk_text_02.Wrap(-1)
        time_sizer.Add(self.bk_text_02, 0, wx.ALL, 5)

        self.m_date_text = wx.StaticText(self, wx.ID_ANY, u"修改服务器日期：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_date_text.Wrap(-1)
        time_sizer.Add(self.m_date_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        m_date_sizer = wx.BoxSizer(wx.HORIZONTAL)

        year_choiceChoices = [wx.EmptyString, u"2018", u"2019", u"2010"]
        self.year_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(55, -1), year_choiceChoices, 0)
        self.year_choice.SetSelection(0)
        m_date_sizer.Add(self.year_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.my_text = wx.StaticText(self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.DefaultSize, 0)
        self.my_text.Wrap(-1)
        m_date_sizer.Add(self.my_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        month_choiceChoices = [wx.EmptyString, u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10",
                               u"11", u"12"]
        self.month_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, month_choiceChoices, 0)
        self.month_choice.SetSelection(0)
        m_date_sizer.Add(self.month_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.mm_text = wx.StaticText(self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0)
        self.mm_text.Wrap(-1)
        m_date_sizer.Add(self.mm_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        day_choiceChoices = [wx.EmptyString, u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10",
                             u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23",
                             u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31"]
        self.day_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, day_choiceChoices, 0)
        self.day_choice.SetSelection(0)
        m_date_sizer.Add(self.day_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.md_text = wx.StaticText(self, wx.ID_ANY, u"日  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.md_text.Wrap(-1)
        m_date_sizer.Add(self.md_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.local_date_btn = wx.Button(self, wx.ID_ANY, u"获取本地日期", wx.DefaultPosition, wx.DefaultSize, 0)
        m_date_sizer.Add(self.local_date_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        time_sizer.Add(m_date_sizer, 1, wx.EXPAND, 5)

        self.m_time_text = wx.StaticText(self, wx.ID_ANY, u"修改服务器时间：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_time_text.Wrap(-1)
        time_sizer.Add(self.m_time_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        m_time_sizer = wx.BoxSizer(wx.HORIZONTAL)

        hour_choiceChoices = [wx.EmptyString, u"00", u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09",
                              u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22",
                              u"23"]
        self.hour_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(55, -1), hour_choiceChoices, 0)
        self.hour_choice.SetSelection(0)
        m_time_sizer.Add(self.hour_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.mh_text = wx.StaticText(self, wx.ID_ANY, u"时", wx.DefaultPosition, wx.DefaultSize, 0)
        self.mh_text.Wrap(-1)
        m_time_sizer.Add(self.mh_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        minute_choiceChoices = [wx.EmptyString, u"00", u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09",
                                u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21",
                                u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31", u"32", u"33",
                                u"34", u"35", u"36", u"37", u"38", u"39", u"40", u"41", u"42", u"43", u"44", u"45",
                                u"46", u"47", u"48", u"49", u"50", u"51", u"52", u"53", u"54", u"55", u"56", u"57",
                                u"58", u"59"]
        self.minute_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, minute_choiceChoices, 0)
        self.minute_choice.SetSelection(0)
        m_time_sizer.Add(self.minute_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.mm_text = wx.StaticText(self, wx.ID_ANY, u"分", wx.DefaultPosition, wx.DefaultSize, 0)
        self.mm_text.Wrap(-1)
        m_time_sizer.Add(self.mm_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        second_choiceChoices = [wx.EmptyString, u"00", u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09",
                                u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21",
                                u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31", u"32", u"33",
                                u"34", u"35", u"36", u"37", u"38", u"39", u"40", u"41", u"42", u"43", u"44", u"45",
                                u"46", u"47", u"48", u"49", u"50", u"51", u"52", u"53", u"54", u"55", u"56", u"57",
                                u"58", u"59"]
        self.second_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, second_choiceChoices, 0)
        self.second_choice.SetSelection(0)
        m_time_sizer.Add(self.second_choice, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.ms_text = wx.StaticText(self, wx.ID_ANY, u"秒  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ms_text.Wrap(-1)
        m_time_sizer.Add(self.ms_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.local_time_btn = wx.Button(self, wx.ID_ANY, u"获取本地时间", wx.DefaultPosition, wx.DefaultSize, 0)
        m_time_sizer.Add(self.local_time_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        time_sizer.Add(m_time_sizer, 1, wx.EXPAND, 5)

        self.bk_text_03 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bk_text_03.Wrap(-1)
        time_sizer.Add(self.bk_text_03, 0, wx.ALL, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.modify_btn = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        btn_sizer.Add(self.modify_btn, 0, wx.ALL, 5)

        self.bk_text_04 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bk_text_04.Wrap(-1)
        btn_sizer.Add(self.bk_text_04, 0, wx.ALL, 5)

        self.cancel_btn = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        btn_sizer.Add(self.cancel_btn, 0, wx.ALL, 5)

        time_sizer.Add(btn_sizer, 1, wx.EXPAND, 5)

        self.SetSizer(time_sizer)
        self.Layout()
        time_sizer.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.ser_choice.Bind(wx.EVT_CHOICE, self.on_choose_server)
        self.local_date_btn.Bind(wx.EVT_BUTTON, self.on_get_local)
        self.local_time_btn.Bind(wx.EVT_BUTTON, self.on_get_local)
        self.modify_btn.Bind(wx.EVT_BUTTON, self.on_modify_time)
        self.cancel_btn.Bind(wx.EVT_BUTTON, self.on_cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_choose_server(self, event):
        event.Skip()

    def on_get_local(self, event):
        event.Skip()

    def on_modify_time(self, event):
        event.Skip()

    def on_cancel(self, event):
        event.Skip()


