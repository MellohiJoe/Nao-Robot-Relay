# coding=utf-8
from naoqi import ALModule

from src.Bot1.Entity.RedBallData import RedBallData


class RedBallMod(ALModule):
    def __init__(self, name):
        ALModule.__init__(self, name)
        self.mod_name = name
        self.call_name = self.fun.__name__
        self._pd = None  # 数据暂存区

    def fun(self, dataName, val, msg):
        pd = RedBallData()
        if val and isinstance(val, list) and len(val) >= 2:
            pd.is_wrong = False
            # timeStamp = val[0]
            ballInfo = val[1]
            centerX = ballInfo[0]
            # centerY = ballInfo[1]
            # sizeX, sizeY = ballInfo[2], ballInfo[3]
            pd.centerX = centerX
        else:
            pd.is_wrong = True

        self._pd = pd

    def get_pop(self):
        pd = self._pd
        self._pd = None
        return pd
