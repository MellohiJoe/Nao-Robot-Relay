# coding=utf-8
import time

from src.Bot2 import modules
from src.Bot2.tasks import walker, waiter, sonar, viewer


def loop():
    sonar.on_enter_loop()
    viewer.on_enter_loop()
    while True:
        # 每隔指定时间控制
        time.sleep(modules.main_loop_secs)
        # 检测终点
        if sonar.detect_to_arrive():
            break

        # 视觉 + 调整方向
        data = viewer.pose_vision()
        walker.adjust_move(data)

    sonar.on_exit_loop()
    viewer.on_exit_loop()


def main():
    # 姿态初始
    walker.init_move()

    # 等待接力
    waiter.wait_to_start()

    # 开始移动
    walker.start_move()

    # ..........主循环 ..........
    loop()

    # 结束动作
    walker.stop_move()

    # 后续处理
    modules.tts.say('任务完成')
    print 'ending ......................'


if __name__ == '__main__':
    main()
