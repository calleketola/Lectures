class Hus():

    def __init__(self, l, b):
        self.längd = l
        self.bredd = b

    def kvadratiskt(self):
        return self.längd == self.bredd

    def yta(self):
        return self.längd*self.bredd

    __yta = yta

    def __str__(self):
        return "Jag är ett hus med storleken "+ str(self.yta()) + " m2"

class Flervåningshus(Hus):

    def __init__(self, l, b, v):
        super().__init__(l,b)
        self.antal = v # Antal våningar

    def höghus(self):
        return self.antal >= 10

    def yta(self):
        return super().yta()*self.antal

class Flerfamiljshus(Flervåningshus):

    def __init__(self, l, b, v, n):
        super().__init__(l,b,v)
        self.lägenheter = n # antalet lägenheter

    def yta(self):
        return super().yta()*0.95

class Skola(Flervåningshus):

    def __init__(self, l, b, v, a):
        super().__init__(l,b,v)
        self.antal_klassrum = a

    def klassrum_våning(self):
        return self.antal_klassrum/self.antal

    def yta(self):
        return self.antal_klassrum*50
