# coding=utf-8
import numpy as np

from src.Bot2.Entity.FlowData import FlowData


class FlowDetectMod:
    def __init__(self, a=(0.0, 0.0), b=(1.0, 1.0)):
        """
        :param flow_threshold: 有效波动阈值
        :param a: 起始点，像素坐标系
        :param b: 起始点，像素坐标系
        """
        self._last = None
        self._flow_th = 0
        self._a = a
        self._b = b

    def begin(self, flow_threshold=20):
        self._last = None
        self._flow_th = flow_threshold

    def get(self, raw1, raw2):
        """
        :param raw1: 1 减 2
        :param raw2:
        :return:
        """
        if raw1 is None or raw2 is None:
            fd = FlowData()
            fd.is_wrong = True
            return fd

        w, h, c = raw1[0:3]
        h0 = int(h * self._a[0])
        w0 = int(w * self._a[0])
        h1 = int(h * self._b[0])
        w1 = int(w * self._b[1])

        arr1 = np.frombuffer(raw1[6], dtype=np.int8)  # debug
        arr2 = np.frombuffer(raw2[6], dtype=np.int8)
        img1 = arr1.reshape(w, h, c)
        img2 = arr2.reshape(w, h, c)

        img1 = img1[w0: w1, h0: h1, :]
        img2 = img2[w0: w1, h0: h1, :]

        # 计算波动
        d = img1 - img2
        d = np.abs(d)
        m = np.mean(d)

        fd = FlowData()
        fd.is_wrong = False
        fd.diff = m
        fd.effective = m > self._flow_th
        return fd

    def update(self, image_remote):
        """
        :param image_remote:
        :return: FlowData已检测有效性
        """
        IR = image_remote
        w, h, c = IR[0:3]
        array = IR[6]
        arr = np.frombuffer(array, dtype=np.uint8)
        img = arr.reshape(w, h, c)
        h0 = int(h * self._a[0])
        w0 = int(w * self._a[0])
        h1 = int(h * self._b[0])
        w1 = int(w * self._b[1])
        # 切分
        img = img[w0: w1, h0: h1, :]
        if self._last is not None:
            d = img - self._last
            d = np.abs(d)
            m = np.mean(d)
            # 分装数据
            fd = FlowData()
            fd.is_wrong = False
            fd.diff = m
            fd.effective = m > self._flow_th
        else:
            fd = FlowData()
            fd.is_wrong = True

        self._last = img
        return fd
