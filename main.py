# coding=utf-8

def choose_bot():
    import sys
    if len(sys.argv) >= 2:
        return int(sys.argv[1])
    else:
        return 1


if __name__ == '__main__':
    if choose_bot() == 1:
        from src.Bot1.Behavior.start import main
        from src.Bot1.modules import *
        main()
    elif choose_bot() == 2:
        from src.Bot2.Behavior.start import main
        from src.Bot2.modules import *
        main()
