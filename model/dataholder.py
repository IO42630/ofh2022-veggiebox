import json


class DataHolder:
    savepath = None
    data = {}

    def __init__(self, savepath):
        self.savepath = savepath

    def save(self):
        f = open("../data/" + self.savepath, "w")
        f.write(json.dumps(self.data))
        f.close()

    def load(self):
        f = open("../data/" + self.savepath, "w")
        self.data = json.load(f)
        f.close()
