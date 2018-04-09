import os
import wx
import cv2
from face.component.CapturePanel import CapturePanel


class CameraPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.createComponents()

    def createComponents(self):
        verticalBox = wx.BoxSizer(wx.VERTICAL)
        tips = wx.StaticText(self, 0, u"摄像头", style=wx.TE_LEFT)

        cameraPanel = wx.Panel(self, -1)
        rstpUrl = 'rtsp://admin:admin2014@192.168.1.7:554/h264/ch1/sub/av_stream'
        cap = cv2.VideoCapture(rstpUrl)
        capturePanel = CapturePanel(cameraPanel, cap)

        verticalBox.Add(tips, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        verticalBox.Add(cameraPanel, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.SetSizer(verticalBox)
