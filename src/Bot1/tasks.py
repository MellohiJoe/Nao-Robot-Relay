# coding=utf-8
import src.Bot1.modules as mod
from src.Bot1.Task.Sensor import Sensor
from src.Bot1.Task.Talker import Talker
from src.Bot1.Task.Waiter import Waiter

sonar = Sensor()
talker = Talker()
waiter = Waiter(sonar, talker)

if mod.FACE:
    from src.Bot1.Task.FaceViewer import FaceViewer
    viewer = FaceViewer()
    from src.Bot1.Task.FaceWalker import FaceWalker
    walker = FaceWalker()
elif mod.RED_BALL:
    from src.Bot1.Task.RedBallViewer import RedBallViewer  # 动态导入
    viewer = RedBallViewer()
else:
    raise Exception("What's wrong with you!")
