# coding=utf-8
from naoqi import ALProxy, ALBroker

from src.Bot1.Mod.HeadMod import HeadMod

IP = '192.168.43.104'
PORT = 9559

# 时间
main_loop_secs = 0.03  # s
red_ball_period = 15  # ms
face_period = 15  # ms

# pdc参数
# kp = 0.8
kp = 0.6

# 关节与运动
interval_secs = 0.3  # s
stand_init_speed = 0.3
stiffness = 0.8
# walk_speed = 0.4
walk_speed = 0.8

# 识别目标启用
FACE = True
RED_BALL = False

# 破解
broker = ALBroker("pythonBroker", "0.0.0.0", 0, IP, PORT)

# 语音
tts = ALProxy("ALTextToSpeech", IP, 9559)

# 运动
posture = ALProxy("ALRobotPosture", IP, 9559)
motion = ALProxy("ALMotion", IP, 9559)

# 视觉
camProxy = ALProxy("ALVideoDevice", IP, PORT)
redBallProxy = ALProxy("ALRedBallDetection", IP, PORT)
faceProxy = ALProxy("ALFaceDetection", IP, PORT)

# 传感器
sonarProxy = ALProxy("ALSonar", IP, 9559)

# 通讯

# 存储
memory = ALProxy("ALMemory", IP, 9559)

# 听觉
recognition = ALProxy("ALSpeechRecognition", IP, 9559)

# 自定义
if RED_BALL:
    from src.Bot1.Mod.RedBallMod import RedBallMod
    redBallMod = RedBallMod('redBallMod')

if FACE:
    from src.Bot1.Mod.FaceMod import FaceMod
    faceMod = FaceMod(memory)

headMod = HeadMod(motion, stiffness)
