# -*- encoding:utf-8 -*-
import time


class HeadMod:
    def __init__(self, motion, stiffness):
        self._speed = 0.2
        self._stiff = stiffness
        self.motion = motion

    def left_down(self):
        self.motion.setStiffnesses("Head", self._stiff)
        self.motion.setAngles("HeadYaw", 1.2, self._speed)
        self.motion.waitUntilMoveIsFinished()
        self.motion.setAngles("HeadPitch", 0.5, self._speed)
        self.motion.waitUntilMoveIsFinished()
        time.sleep(2)

    def middle(self):
        self.motion.setStiffnesses("Head", self._stiff)
        self.motion.setAngles("HeadYaw", 0.0, self._speed)
        self.motion.waitUntilMoveIsFinished()
        self.motion.setAngles("HeadPitch", 0.0, self._speed)
        self.motion.waitUntilMoveIsFinished()
        time.sleep(2)

    def right_down(self):
        self.motion.setStiffnesses("Head", self._stiff)
        self.motion.setAngles("HeadYaw", -1.2, self._speed)
        self.motion.waitUntilMoveIsFinished()
        self.motion.setAngles("HeadPitch", 0.5, self._speed)
        self.motion.waitUntilMoveIsFinished()
        time.sleep(2)

    def right(self):
        self.diy(-3.14159 / 2, 0.0)

    def down(self):
        self.diy(0.0, 0.5)

    def diy(self, yaw, pitch):
        self.motion.setStiffnesses("Head", self._stiff)
        self.motion.setAngles("HeadYaw", yaw, self._speed)
        self.motion.waitUntilMoveIsFinished()
        self.motion.setAngles("HeadPitch", pitch, self._speed)
        self.motion.waitUntilMoveIsFinished()
        time.sleep(2)
