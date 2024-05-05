# coding=utf-8

class BotEvents:
    def __init__(self):
        pass

    def init_move(self):
        """
        :desc:到预备姿态
        :time: 几秒，阻塞
        :return:无
        """

    def wait_to_start(self):
        """
        :desc:检测开始信号（超声波，声音，其他），若没有一直等
        :time: 持续耗时，循环+阻塞
        :return:无
        """

    def start_move(self):
        """
        :desc:从静止开始前进
        :time: 极快，可短暂阻塞
        :return:无
        """

    def on_enter_loop(self):
        """
        :desc:进入主循环事件回调接口
        - 例如以下：
            - 开始视觉
            - 开始超声波
        - 由任务各自实现，主流程中调用
        :time: 瞬间，不阻塞
        :return: 无
        """

    def on_exit_loop(self):
        """
        :desc:退出主循环事件回调接口
        - 例如以下：
            - 结束视觉
            - 结束超声波
        :time: 瞬间，不阻塞
        :return: 无
        """

    def pose_vision(self):
        """
        :desc:视觉检测出Nao运动的偏移角度
        :time: 瞬间，不阻塞
        :return: 红球或人脸位姿，参考对应实体类
        """

    def adjust_move(self, data):
        """
        :desc:根据当前机器人的位姿，调整移动方向
        :param data: 由pose_vision返回的
        :time: 瞬间，不阻塞
        :return:无
        """

    def detect_to_arrive(self):
        """
        :desc:判定是否达到终点
        :time: 瞬间，不阻塞
        :return: True或者False
        """

    def call_friend(self):
        """
        :desc:发送信号，呼叫同伴
        :time: 阻塞
        :return: 无
        """

    def stop_move(self):
        """
        :desc:停止移动
        :time: 未知
        :return:无
        """
