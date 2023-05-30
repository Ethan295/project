class Stufa:
    accesa = False

    def __init__(self):
        self.accesa = False

    def Acecendi(self):
        self.accesa = True

    def Spegni(self):
        self.accesa = False

    def Inverso(self):
        if self.accesa:
            self.accesa = False
        else:
            self.accesa = True

    def toString(self):
        print("Stufa accesa") if self.accesa else print("Stufa spenta")



s = Stufa()
s.toString()
s.Acecendi()
s.toString()
s.Spegni()
s.toString()
s.Inverso()
s.toString()
s.Inverso()
s.toString()



"""
Fatto meglio

 def inverso(self):
        self.accesa = not self.accesa
        
"""