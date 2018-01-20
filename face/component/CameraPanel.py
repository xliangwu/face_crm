import os
import wx


class CameraPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.createComponents()

    def createComponents(self):
        verticalBox = wx.BoxSizer(wx.VERTICAL)
        tips = wx.StaticText(self, 0, u"摄像头", style=wx.TE_LEFT)
        verticalBox.Add(tips, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.SetSizer(verticalBox)
