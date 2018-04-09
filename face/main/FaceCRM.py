import wx
import sys
import wx.lib.scrolledpanel as scrolled
from wx.lib.pubsub import pub
from face.config.UIConfig import configConst
from face.component.CameraPanel import CameraPanel
from face.component.FaceRecognizePanel import FaceRecognizePanel
from face.component.FaceSocketServerThread import FaceSocketServerThread
import wx


class FaceManagerFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(FaceManagerFrame, self).__init__(*args, **kw)
        self.facePanels = []
        # create panels in the frame
        self.createPanels()

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText(configConst.SYSTEM_WELCOME_INFO)

        pub.subscribe(self.refreshFaceImage, 'face.refresh')

        # start backend threads
        FaceSocketServerThread('192.168.1.130', 6789)

    def refreshFaceImage(self, index, blackData, realData, time=None):
        print('Will refresh face image :[%s]' % index)
        self.facePanels[int(index)].refreshImage(blackData, realData)

    def createPanels(self):
        scrolledPanel = scrolled.ScrolledPanel(self, size=(425, 400))

        cameraPanelOne = CameraPanel(scrolledPanel, -1)
        cameraPanelTwo = CameraPanel(scrolledPanel, -1)

        faceRecognizePanelOne = FaceRecognizePanel(scrolledPanel, -1)
        faceRecognizePanelTwo = FaceRecognizePanel(scrolledPanel, -1)

        outBoxSize = wx.BoxSizer(wx.VERTICAL)
        boxSize0 = wx.BoxSizer(wx.HORIZONTAL)
        boxSize1 = wx.BoxSizer(wx.HORIZONTAL)

        boxSize0.Add(cameraPanelOne, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        boxSize0.Add(faceRecognizePanelOne, proportion=0, flag=wx.ALL, border=2)
        boxSize1.Add(cameraPanelTwo, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        boxSize1.Add(faceRecognizePanelTwo, proportion=0, flag=wx.ALL, border=2)
        outBoxSize.Add(boxSize0, proportion=0, flag=wx.EXPAND | wx.ALL, border=2)
        outBoxSize.Add(boxSize1, proportion=0, flag=wx.EXPAND | wx.ALL, border=2)
        self.facePanels.append(faceRecognizePanelOne)
        self.facePanels.append(faceRecognizePanelTwo)

        scrolledPanel.SetSizer(outBoxSize)
        scrolledPanel.Layout()
        scrolledPanel.SetupScrolling(scroll_x=True)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(scrolledPanel, proportion=1, flag=wx.EXPAND)
        self.SetSizer(mainSizer)
        self.Fit()

    def makeMenuBar(self):
        memberMenu = wx.Menu()
        editItem = memberMenu.Append(-1, configConst.MENU_MEMBER_EDIT)
        memberMenu.AppendSeparator()
        exitItem = memberMenu.Append(wx.ID_EXIT, configConst.MENU_MEMBER_QUIT)

        viewMenu = wx.Menu()

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT, configConst.MENU_HELP_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(memberMenu, configConst.MENU_MEMBER)
        menuBar.Append(viewMenu, configConst.MENU_VIEW)
        menuBar.Append(helpMenu, configConst.MENU_HELP)

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.onEdit, editItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitItem)
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)

    def onExit(self, event):
        self.Close(True)

    def onEdit(self, event):
        wx.MessageBox("Hello again from wxPython")

    def onAbout(self, event):
        wx.MessageBox(configConst.MENU_HELP_ABOUT_INFO, configConst.MENU_HELP_ABOUT_TITLE,
                      wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App()
    frm = FaceManagerFrame(None, title=configConst.SYSTEM_TITLE)
    frm.Show()
    app.MainLoop()
