class FaceData:
    def __init__(self):
        self.alpha = 0.0  # = centerX  -0.34 ~ +0.34
        self.beta = 0.0  # = centerY -0.34 ~ +0.34
        self.sizeX = 0.0
        self.sizeY = 0.0
        self.faceID = 0
        self.scoreReco = 0.0
        self.faceLabel = ''
        self.timeStampSecs = 0.0
        self.is_wrong = False

    def __str__(self):
        return str({'is_wrong': self.is_wrong, 'alpha': self.alpha, 'faceID': self.faceID})
