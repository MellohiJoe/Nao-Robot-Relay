# coding=utf-8
from naoqi import ALProxy, ALBroker

from src.Bot2.Mod.HeadMod import HeadMod
from src.Bot2.Mod.FaceMod import FaceMod
from src.Bot2.Mod.FlowDetectMod import FlowDetectMod

IP = '192.168.43.115'
PORT = 9559

# 时间
main_loop_secs = 0.03  # s
red_ball_period = 15  # ms
face_period = 15  # ms

# pdc参数
# kp = 0.8
kp = 0.6

# 关节与运动
interval_secs = 1.0  # s
stand_init_speed = 0.3
stiffness = 0.8
# walk_speed = 0.8
walk_speed = 0.4
# neck_turn_toward = ''
neck_turn_toward = 'left'  # 左下
# neck_turn_toward = 'right'  # 右下


# 视频图像
resolution = 0  # 160 x 120px
# resolution = 1  # 320 x 240
# resolution = 2  # 640 x 480
# resolution = 3  # 1280 x 960
colorSpace = 7  # S饱和度
# colorSpace = 11  # RGB
# colorSpace = 12  # HSY

# 破解
broker = ALBroker("pythonBroker", "0.0.0.0", 0, IP, PORT)

# 语音
tts = ALProxy("ALTextToSpeech", IP, 9559)

# 运动
posture = ALProxy("ALRobotPosture", IP, 9559)

motion = ALProxy("ALMotion", IP, 9559)

# 视觉
camProxy = ALProxy("ALVideoDevice", IP, PORT)
faceProxy = ALProxy("ALFaceDetection", IP, PORT)

# 传感器
sonarProxy = ALProxy("ALSonar", IP, 9559)

# 通讯

# 存储
memory = ALProxy("ALMemory", IP, 9559)

# 自定义
faceMod = FaceMod(memory)
flowDetect = FlowDetectMod(a=(0.0, 0.0), b=(1.0, 1.0))
headMod = HeadMod(motion, stiffness)
