# not map function haha
class Map:
    def __init__(self) -> None:
        self.indexList = []
        self.valueList = []

    def set(self, index, value) -> None:
        if self.indexList.count(index) != 0:
            self.valueList[self.indexList.index(index)] = value
        self.indexList.append(index)
        self.valueList.append(value)

    def pop(self, index) -> None:
        self.indexList.pop(index)
        self.valueList.pop(index)

    def get(self, index):
        return self.valueList[self.indexList.index(index)]
