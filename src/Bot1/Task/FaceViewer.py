# coding=utf-8

from src.Bot1 import modules
from src.Bot1.BotEvents import BotEvents
from src.Bot1.Entity.FaceData import FaceData
from src.Bot1.modules import camProxy, faceProxy, faceMod


class FaceViewer(BotEvents):
    def __init__(self):
        BotEvents.__init__(self)
        self._pmo_secs = 0.1  # s，一段时间
        self._pmo_rate = 0.7  # 命中率最低保证
        self._is_pmo = False  # 人脸已保证
        self._hits = []

    def _check_pmo(self, fd):
        if fd is None or fd.is_wrong:
            self._hits.append(0)
        else:
            self._hits.append(1)

        count = len(self._hits)
        duration = count * modules.main_loop_secs  # 累计时间
        if duration >= self._pmo_secs:
            rate = sum(self._hits) / float(count)
            print self._pmo_secs, '秒，人脸存在比率', rate  # for test
            self._hits = []  # 清空列表
            if rate >= self._pmo_rate:  # 大于70%
                self._faceId = fd.faceID
                return True

        return False

    def pose_vision(self):
        if self._is_pmo:
            faceMod.update()  # 提取内存值
            fd = faceMod.get()
            faceMod.pop()  # 拿走，确保不留存
        else:
            faceMod.update()
            fd = faceMod.get()
            faceMod.pop()
            if self._check_pmo(fd):
                self._is_pmo = True
                print '-------------------------'
                print '人脸识别通过，已持续检测到人脸'
                print '-------------------------'
                modules.tts.post.say('人脸锁定')
            else:
                fd = None

        # 返回值保证
        if fd is None:
            fd = FaceData()
            fd.is_wrong = True

        return fd

    def on_enter_loop(self):
        # 开始视觉功能
        print '开始视觉任务'
        camProxy.setActiveCamera(0)
        faceProxy.subscribe("Test_Face", modules.face_period, 0.0)
        self._is_pmo = False  # 待保证人脸
        faceMod.set(faceID=None)

    def on_exit_loop(self):
        faceProxy.unsubscribe("Test_Face")
