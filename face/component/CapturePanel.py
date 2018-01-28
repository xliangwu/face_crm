import cv2
import wx


class CapturePanel(wx.Panel):
    def __init__(self, parent, capture, fps=72):
        wx.Panel.__init__(self, parent, wx.ID_ANY, (0, 0), (400, 300))

        self.capture = capture
        if self.capture.isOpened():
            ret, frame = self.capture.read()
            height, width = frame.shape[:2]
            print(width, height)

            parent.SetSize((width, height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self.bmp = wx.Bitmap.FromBuffer(width, height, frame)

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
                self.bmp.CopyFromBuffer(frame)
                self.Refresh()
