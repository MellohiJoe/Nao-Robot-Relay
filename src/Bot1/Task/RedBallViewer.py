# coding=utf-8

from src.Bot1 import modules
from src.Bot1.BotEvents import BotEvents
from src.Bot1.Entity.RedBallData import RedBallData
from src.Bot1.modules import camProxy, redBallProxy, memory, redBallMod, tts


class RedBallViewer(BotEvents):
    def vision_to_start(self):
        print 'WARNING: Red ball is not suggested for tracing, and will not be promised!'

    def on_enter_loop(self):
        tts.say('start vision by red ball')
        camProxy.setActiveCamera(1)
        redBallProxy.subscribe("Test_RedBall", modules.red_ball_period, 1.0)
        memory.subscribeToEvent('redBallDetected', redBallMod.mod_name, redBallMod.call_name)

    def on_exit_loop(self):
        memory.unsubscribeToEvent('redBallDetected', redBallMod.mod_name)
        redBallProxy.unsubscribe("Test_RedBall")  # ~订阅

    def pose_vision(self):
        # 每隔一段时间查询，和拿走
        pd = redBallMod.get_pop()
        print 'pose_vision DEBUG:', pd.is_wrong, pd.centerX
        if pd is None:
            pd = RedBallData()
            pd.is_wrong = True

        return pd
