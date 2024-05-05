class FlowData:
    def __init__(self):
        self.diff = 0.0
        self.effective = False
        self.is_wrong = False

    def __str__(self):
        if self.is_wrong:
            return '(is_wrong)'
        return '(ok, {}, effective: {})'.format(self.diff, self.effective)
