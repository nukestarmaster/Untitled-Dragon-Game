class Event():
    def __init__(self, effect, cond = lambda : True, cost = []):
        self.effect = effect
        self.cond = cond
        self.cost = cost

    def valid(self):
        if self.cond() == False:
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
            self.effect()