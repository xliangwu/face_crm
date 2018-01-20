import wx
import os
import base64


class FaceRecognizePanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.bitMapList = []

        self.createComponents()
        self.SetMaxSize((860, 460))

    def createComponents(self):
        gridSizer = wx.GridSizer(2, 4, 5, 5)

        curDir = os.getcwd()
        defaultImage = curDir + '/default.jpg'
        for i in range(0, 8):
            image = wx.Image(defaultImage, wx.BITMAP_TYPE_JPEG)
            bitmap = image.ConvertToBitmap()

            panel = wx.Panel(self)
            panel.bmp = wx.StaticBitmap(parent=panel, bitmap=bitmap)
            self.bitMapList.append(panel.bmp)
            gridSizer.Add(panel, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)

        # button = wx.Button(self, wx.ID_ANY, 'change image')
        # button.Bind(wx.EVT_BUTTON, self.refreshImage)
        # gridSizer.Add(button, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)

        self.SetSizer(gridSizer)

    def refreshImage(self, blackData='', realData=''):
        print("Refresh images")
        curDir = os.getcwd()

        for i in range(0, 8):
            defaultImage = curDir + '/some_image.jpg'
            image = wx.Image(defaultImage, wx.BITMAP_TYPE_JPEG)
            bitmap = image.ConvertToBitmap()

            self.bitMapList[i].SetBitmap(bitmap)
        self.Refresh()

    def convertBase64ToImage(self, data, output):
        imageData = base64.decodebytes(data)
        with open(output, 'wb') as f:
            f.write(imageData)
