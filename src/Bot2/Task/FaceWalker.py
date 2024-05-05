# coding=utf-8
import time

import src.Bot2.modules as mod
from src.Bot2.BotEvents import BotEvents
from src.Bot2.Entity.FaceData import FaceData


class FaceWalker(BotEvents):
    def __init__(self):
        BotEvents.__init__(self)
        self._x = mod.walk_speed  # x方向速度
        self._y = 0.0  # y方向速度
        self._frequency = 0.5  # 步态参数,可以分别设置左脚和右脚的步态参数
        self._kp = mod.kp

    def init_move(self):
        print '初始移动'
        # 将其刚化
        mod.motion.setStiffnesses("Body", mod.stiffness)
        time.sleep(mod.interval_secs)
        # 首先唤醒NAO
        mod.motion.wakeUp()
        time.sleep(mod.interval_secs)
        # 让NAO站好
        mod.posture.goToPosture("StandInit", mod.stand_init_speed)
        time.sleep(mod.interval_secs)
        # 头部补充
        if mod.neck_turn_toward == 'left':
            mod.headMod.left_down()
        elif mod.neck_turn_toward == 'right':
            mod.headMod.right_down()
        # 初始化
        mod.motion.moveInit()
        time.sleep(mod.interval_secs)
        print '初始移动OK'

    def start_move(self):
        mod.headMod.middle()
        mod.motion.moveToward(self._x, self._y, 0.0, [["Frequency", self._frequency]])

    def _pid(self, x):
        y = x * self._kp
        y = min(y, 1.0)
        y = max(-1.0, y)
        return y

    def adjust_move(self, data):
        if not isinstance(data, FaceData):
            raise Exception('数据类型异常(Walker)', data)

        if not data.is_wrong:
            theta = self._pid(data.alpha)
            mod.motion.moveToward(self._x, self._y, theta, [["Frequency", self._frequency]])
        else:
            print 'data.is_wrong(Walker):', str(data)

    def stop_move(self):
        # 停止机器人行走
        print '停止移动'
        mod.motion.stopMove()
        mod.posture.goToPosture("Crouch", 0.3)
