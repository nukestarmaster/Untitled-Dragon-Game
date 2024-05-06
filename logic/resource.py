
class Resource():
    def __init__(self, name, max = None):
        self.name = name
        self.amount = 0
        self.max = max
    
    def __add__(self, increase):
        if self.max is not None:
            self.amount = min(self.amount + increase, self.max)
            return self
        self.amount += increase
        return self
    
    def __sub__(self, decrease):
        if decrease > self.amount:
            return self
        self.amount -= decrease
        return self
    
    def __str__(self):
        if self.max is not None:
            return f"{self.name}: {self.amount}/{self.max}"
        return f"{self.name}: {self.amount}"