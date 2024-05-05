# coding=utf-8
import time

from src.Bot2.BotEvents import BotEvents
from src.Bot2.modules import sonarProxy, memory  # 从全局模块中引入


class Sensor(BotEvents):
    def __init__(self):
        BotEvents.__init__(self)

    def wait_to_start(self):
        sonarProxy.subscribe("myApplication")
        while True:
            # 左右前方无障碍
            if memory.getData("Device/SubDeviceList/US/Left/Sensor/Value") > 0.2 and memory.getData(
                    "Device/SubDeviceList/US/Right/Sensor/Value") > 0.2:
                break
            time.sleep(1)
        sonarProxy.unsubscribe("myApplication")

    def on_enter_loop(self):
        sonarProxy.subscribe("Test_Sonar")

    def on_exit_loop(self):
        sonarProxy.unsubscribe("Test_Sonar")

    def detect_to_arrive(self):
        # 若前方有障碍
        if memory.getData("Device/SubDeviceList/US/Left/Sensor/Value") < 0.2 or memory.getData(
                "Device/SubDeviceList/US/Right/Sensor/Value") < 0.2:
            return True

        return False
