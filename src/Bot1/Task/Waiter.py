# coding=utf-8
from src.Bot1.BotEvents import BotEvents


class Waiter(BotEvents):

    def __init__(self, sonar, talker):
        BotEvents.__init__(self)
        if not isinstance(sonar, BotEvents) or not isinstance(talker, BotEvents):
            raise Exception

        self.sonar = sonar
        self.talker = talker

    def detect_to_start(self):
        print '超声'
        self.sonar.detect_to_start()
        print '语音'
        self.talker.detect_to_start()
