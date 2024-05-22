class Event():
    def __init__(self, effect = None, cond = None, cost = []):
        self.effect = effect
        self.cond = cond
        self.cost = cost

    def valid(self):
        if self.cond != None and self.cond() == False:
            return False
        for c in self.cost:
            if not c[0].can_spend(c[1]):
                return False
        return True

    def spend_cost(self):
        for c in self.cost:
            c[0] - c[1]

    def __call__(self):
        if self.valid():
            self.spend_cost()
            if self.effect is not None:
                self.effect()