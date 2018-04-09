import cv2
import wx
from face.config.UIConfig import configConst


class CapturePanel(wx.Panel):
    def __init__(self, parent, capture, fps=72):

        wx.Panel.__init__(self, parent, wx.ID_ANY, (0, 0), (configConst.CAPTURE_WIDTH, configConst.CAPTURE_HEIGHT))

        self.capture = capture
        if self.capture.isOpened():
            ret, frame = self.capture.read()
            height, width = frame.shape[:2]

            # parent.SetSize((width, height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            inputBmp = wx.Bitmap.FromBuffer(width, height, frame)
            inputImg = inputBmp.ConvertToImage()
            image = inputImg.Scale(configConst.CAPTURE_WIDTH, configConst.CAPTURE_HEIGHT, wx.IMAGE_QUALITY_HIGH)
            convertBmp = wx.Bitmap(image)
            self.bmp = convertBmp

            self.timer = wx.Timer(self)
            self.timer.Start(1000. / fps)

            self.Bind(wx.EVT_PAINT, self.OnPaint)
            self.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        if self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width = frame.shape[:2]
                inputBmp = wx.Bitmap.FromBuffer(width, height, frame)
                inputImg = inputBmp.ConvertToImage()
                image = inputImg.Scale(configConst.CAPTURE_WIDTH, configConst.CAPTURE_HEIGHT, wx.IMAGE_QUALITY_HIGH)
                convertBmp = wx.Bitmap(image)
                self.bmp = convertBmp
                self.Refresh()
