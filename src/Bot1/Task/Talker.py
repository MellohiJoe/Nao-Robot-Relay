# coding=utf-8
import time

from src.Bot1.BotEvents import BotEvents
from src.Bot1.modules import memory, recognition, tts, motion  # 从全局模块中引入


def clear(s):
    return s.strip('<...>').strip()


class Talker(BotEvents):

     def detect_to_start(self):
        recognition.pause(True)
        # 设置语言和词汇
        recognition.setLanguage("English")
        recognition.setVocabulary(["Start", "Move", "one", "two", "three"], False)  # 设置识别词汇为 "开始"

        # 启动识别器
        recognition.subscribe("SpeechRecognition1")

        try:
            tts.say("请下指令")
            motion.stopMove()
            while True:
                word = memory.getData("WordRecognized")
                word[0] = clear(word[0])  # debug
                print(word[0])
                time.sleep(0.3)
                if word[0] == "Move":
                    tts.say("开始移动")
                    return True
                if word[0] == "Start":
                    time.sleep(1)
                if word[0] == "one":
                    time.sleep(1)
                if word[0] == "two":
                    time.sleep(1)
                if word[0] == "three":
                    time.sleep(1)

        finally:
            # 在程序被中断时取消订阅并清理资源
            recognition.unsubscribe("SpeechRecognition1")
