class Stack():
    def __init__(self):
        self.__self = []
        self.__size = 0
        super().__init__()
    
    def push(self, obj: object):
        self.__self.append(obj)
        self.__size += 1

    def pop(self):
        try:
            self.__self.pop(self.__size - 1)
            self.__size -= 1
        except IndexError:
            'Empty Stack Popped!'
            pass
    
    def top(self):
        try:
            return self.__self[self.__size - 1]
        except IndexError:
            'Empty Stack don\'t have top!'
            pass

    def empty(self): return self.__size == 0

    def toList(self): return self.__self

    def size(self): return self.__size