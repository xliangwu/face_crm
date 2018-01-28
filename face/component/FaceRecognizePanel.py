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
        print("BlackData:",blackData)

        # FIFO
        self.bitMapList[3].SetBitmap(self.bitMapList[2].GetBitmap())
        self.bitMapList[7].SetBitmap(self.bitMapList[6].GetBitmap())
        self.bitMapList[2].SetBitmap(self.bitMapList[1].GetBitmap())
        self.bitMapList[6].SetBitmap(self.bitMapList[5].GetBitmap())
        self.bitMapList[1].SetBitmap(self.bitMapList[0].GetBitmap())
        self.bitMapList[5].SetBitmap(self.bitMapList[4].GetBitmap())

        # 0 & 4
        blackImage = self.convertBase64ToImage(blackData, 'black')
        blackWxImage = wx.Image(blackImage, wx.BITMAP_TYPE_JPEG)
        blackBitmap = blackWxImage.ConvertToBitmap()
        self.bitMapList[0].SetBitmap(blackBitmap)

        realImage = self.convertBase64ToImage(realData, 'real')
        realWxImage = wx.Image(realImage, wx.BITMAP_TYPE_JPEG)
        realBitmap = realWxImage.ConvertToBitmap()
        self.bitMapList[4].SetBitmap(realBitmap)

        self.Refresh()

    def convertBase64ToImage(self, data, name):
        curDir = os.getcwd()
        output = curDir + '/' + name + '.jpg'
        try:
            imageData = base64.decodebytes(str.encode(data))
            with open(output, 'wb') as f:
                f.write(imageData)
            print("Save image :", output)
            return os.path.abspath(output)
        except Exception as error:
            print("Convert base64 string to image failed with ", error)
            return curDir + '/some_image.jpg'
