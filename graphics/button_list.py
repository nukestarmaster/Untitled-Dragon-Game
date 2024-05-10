from typing import Iterable


class Buttton_List():
    def __init__(self, list, x, y, seperation):
        self.list = list
        self.x = x
        self.y = y
        self.seperation = seperation

    def __getitem__(self, index):
        return self.list[index]

    def __add__(self, other):
        if type(other) is list:
            self.list.extend(other)
            return self
        self.list.append(other)
        return self
    
    def __sub__(self, other):
        if type(other) is list:
            for o in other:
                self.list.remove(o)
            return self
        self.list.remove(other)
        return self
    
    def draw(self):
        pass