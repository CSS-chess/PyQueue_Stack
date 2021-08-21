class Queue():
    def __init__(self):
        self.__self = []
        self.__size = 0
        super().__init__()
    
    def push(self, obj: object):
        self.__self.append(obj)
        self.__size += 1

    def pop(self):
        try:
            self.__self.pop(0)
            self.__size -= 1
        except IndexError:
            'Empty Queue Popped!'
            pass
    
    def front(self):
        try:
            return self.__self[0]
        except IndexError:
            'Empty Queue don\'t have front!'
            pass

    def empty(self): return self.__size == 0

    def toList(self): return self.__self

    def size(self): return self.__size