# coding=utf-8
import time

from src.Bot2.BotEvents import BotEvents
from src.Bot2.modules import camProxy, tts, flowDetect
import src.Bot2.modules as mod


def calc_rate(recent, dont_need):
    cnt = 0
    for e in recent:
        if e.is_wrong:
            pass
        elif e.effective ^ dont_need:
            cnt += 1

    return float(cnt) / len(recent)


class Waiter(BotEvents):
    def __init__(self):
        BotEvents.__init__(self)
        # self._per_sec = 0.1  # s
        self._fps = 10  # 帧数/秒
        self._keep_sec = 1.6  # s 持续时长，有无波动共用
        self._active_perc = 0.7  # 有波动，最低比率
        self._freeze_perc = 0.7  # 无波动，最低比率
        self._state = 0  # 接近状态
        self._min_sec = 0.8  # s
        self._max_sec = 1.6  # s

    def _select_cand(self, queue, stamp, t0):
        cand = None
        tt = 0
        i = len(queue) - 1
        while i >= 0:
            if self._max_sec >= t0 - stamp[i] >= self._min_sec:  # 0.8s 到 1.6s 之间
                tt = t0 - stamp[i]
                cand = queue[i]
                break

            i = i - 1

        print '@@@@@@', tt, 'cand之后 #len:', len(stamp[i:])
        return cand

    def _select_recent(self, flows, stamp, t0):
        i = len(flows) - 1
        recent = []
        while i >= 0:
            if t0 - stamp[i] <= self._keep_sec:  # 一段时间内
                recent.append(flows[i])  # 变动情况加入
            else:
                break

            i = i - 1

        return recent

    def _state_to_active(self, recent):
        rate = calc_rate(recent, False)
        if rate >= self._active_perc:
            self._state = 1
            tts.post.say('目标接近')

        return False

    def _state_to_freeze(self, recent):
        rate = calc_rate(recent, True)
        if rate >= self._freeze_perc:
            go = True
        else:
            go = False

        return go

    def _detect_flow(self, videoClient):
        flowDetect.begin(flow_threshold=20)
        # need = int(math.ceil(self._keep_sec / self._per_sec))  # 需要多少个时间点
        queue = []
        stamp = []
        flows = []
        self._state = 0  # 初始状态
        t_last = 0
        while True:
            img = camProxy.getImageRemote(videoClient)
            t0 = time.time()
            # 时间戳选择
            queue.append(img)
            stamp.append(t0)
            # 候选出前一张图
            cand = self._select_cand(queue, stamp, t0)
            # 评估变动值
            fd = flowDetect.get(img, cand)
            flows.append(fd)
            print 'FlowData', str(fd)

            # 持续性波动 - TODO:未测试
            recent = self._select_recent(flows, stamp, t0)
            print 'recent #len:', len(recent)
            go = False
            if len(recent) >= 3:  # 可有意义统计
                if self._state is 0:
                    go = self._state_to_active(recent)
                elif self._state is 1:
                    go = self._state_to_freeze(recent)

            print 'state', self._state
            # 通过
            if go:
                return

    def wait_to_start(self):
        print '等待接力'
        camProxy.setActiveCamera(0)  # 用头部看
        videoClient = camProxy.subscribe("Test_VideDevice", mod.resolution, mod.colorSpace, self._fps)
        tts.say('开始等待接力')
        try:
            # 开始检测
            self._detect_flow(videoClient)
            print '成功检测！'
        finally:
            print 'INFO: camProxy unsubscribe!'
            camProxy.unsubscribe(videoClient)
