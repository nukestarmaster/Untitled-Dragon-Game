
class Resource():
    def __init__(self, name, max = None, regen = 0):
        self.name = name
        self.amount = 0
        self.max = max
        self.regen = regen
    
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
            return f"{self.name}: {int(self.amount)}/{self.max}"
        return f"{self.name}: {int(self.amount)}"
    
    def tick(self):
        self + self.regen

    def can_spend(self, decrease):
        return decrease < self.amount