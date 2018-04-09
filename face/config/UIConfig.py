class ConfigConst:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


configConst = ConfigConst()
configConst.SYSTEM_TITLE = "门禁管理系统 V 0.0.1"
configConst.SYSTEM_WELCOME_INFO = "欢迎使用门禁管理系统"

# menu
configConst.MENU_MEMBER = "&人员管理"
configConst.MENU_MEMBER_EDIT = "&编辑 ...\tCtrl+E"
configConst.MENU_MEMBER_QUIT = "&退出 ...\tCtrl+Q"
configConst.MENU_VIEW = "&分析"
configConst.MENU_HELP = "&帮助"
configConst.MENU_HELP_ABOUT = "&关于我们"
configConst.MENU_HELP_ABOUT_TITLE = "关于我们"
configConst.MENU_HELP_ABOUT_INFO = """
门禁管理系统
"""

# canmeral
# capture input is 1280*720 640/360
configConst.CAPTURE_WIDTH = 640
configConst.CAPTURE_HEIGHT = 360
