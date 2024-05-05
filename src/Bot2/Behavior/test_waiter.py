# coding=utf-8

from src.Bot2.tasks import waiter, walker


def main():
    walker.init_move()
    # 启动检测
    waiter.wait_to_start()
    print '我是下一步'


if __name__ == '__main__':
    main()
