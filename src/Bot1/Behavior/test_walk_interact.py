# coding=utf-8
import time

import src.Bot1.modules as mod
from src.Bot1.tasks import walker, sonar


def loop():
    sonar.on_enter_loop()
    while True:
        # 每隔指定时间控制
        time.sleep(mod.main_loop_secs)
        # 检测终点
        if sonar.detect_to_arrive():
            break

        # 视觉 + 调整方向

    sonar.on_exit_loop()


def main():
    print '测试示例'
    # 姿态初始
    walker.init_move()

    # 开始移动
    walker.start_move()  # 暂时非阻塞

    # ..........主循环 ..........
    loop()

    # 结束动作
    walker.stop_move()

    # 后续处理
    print 'ending ......................'


if __name__ == '__main__':
    main()
