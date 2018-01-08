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
configConst.SYSTEM_TITLE = "管理系统 V-0.1"
