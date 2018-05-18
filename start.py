# -*- coding: utf-8 -*-
import wx
from fesui import FesRootFrame

"""
-D 打包成文件夹，默认选择
-F 打包成单个exe文件
-w 启动exe时不启动命令行窗口
-i 指定exe图标
-p 指定打包文件
pyinstaller -F -w start.py -i resource/fa.ico -p fbui/aae076dialog.py -p fbui/b9999dialog.py -p fbui/delchekdialog.py -p fbui/rootframe.py -p resource/fa.ico -p dbapi.py -p fesbusi.py -p feslogs.py -p fesrequests.py -p fesui.py -p settings.py -p utils.py
"""
app = wx.App()
rf = FesRootFrame(None)
rf.Show()
app.MainLoop()
