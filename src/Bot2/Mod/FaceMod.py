# coding=utf-8
from src.Bot2.Entity.FaceData import FaceData


class FaceMod:
    def __init__(self, memory):
        self.memory = memory
        self._fd = None
        self._faceID = None  # 指定人脸

    def update(self):
        """如果没有值，就不更新
        :param val:
        :return:
        """
        val = self.memory.getData('FaceDetected')
        if val and isinstance(val, list) and len(val) >= 2:  # 可根据列表属性，判断有无脸
            # 解构列表数据
            timeStamp = val[0]
            faceInfoArray = val[1]
            t = []
            for j in range(len(faceInfoArray) - 1):
                faceInfo = faceInfoArray[j]
                shapeInfo, extraInfo = faceInfo
                fd = FaceData()
                fd.faceID = extraInfo[0]
                fd.scoreReco = extraInfo[1]
                fd.faceLabel = extraInfo[2]
                fd.alpha = shapeInfo[1]
                fd.beta = shapeInfo[2]
                fd.sizeX = shapeInfo[3]
                fd.sizeY = shapeInfo[4]
                fd.timeStampSecs = timeStamp[0] + timeStamp[1] / 1000000.0
                t.append(fd)

            # 可能要筛选
            if len(t) == 0:
                fd = FaceData()
                fd.is_wrong = True
            else:
                if self._faceID is None:
                    if len(t) != 1:
                        fd = FaceData()
                        fd.is_wrong = True
                    else:
                        fd = t[0]
                else:
                    # 特定的人脸
                    fd = FaceData()
                    fd.is_wrong = True
                    for face in t:
                        if face.faceID == self._faceID:
                            fd = face
                            fd.is_wrong = False
                            break

            self._fd = fd

    def get(self):
        return self._fd

    def set(self, faceID):
        self._faceID = faceID

    def pop(self):
        self._fd = None
