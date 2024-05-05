# coding=utf-8

from src.Bot1.Task.Talker import Talker


def main():
    waiter = Talker()
    # 启动检测
    waiter.detect_to_start()
    print '我是下一步'


if __name__ == '__main__':
    main()
