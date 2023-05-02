class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()
    
    def stabilize(self):
        for _ in range(1000):
            self.next()
    
    def next(self):
        pass


class LogisticMap(Chaos):
    def __init__(self, mu, state):
        super().__init__(mu, state)
    
    def next(self):
        x = self.state
        self.state = self.mu * x * (1 - x)
        return self.state

o = LogisticMap(2, 0.1)
print(o.next(), o.next(), o.next())