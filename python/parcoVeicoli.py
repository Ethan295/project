
class parcoVeicoli:

    luogo = ""
    v2ruote = []
    v4ruote = []


    def __init__(self):
        pass

    def ParcoVeicoli(self, luogo):
        self.luogo = luogo

    def add2Ruote(self, v2):
        self.v2ruote.append(v2)

    def add4Ruote(self,v4):
        self.v4ruote.append(v4)

    def getContenuto(self):
        if len(self.v2ruote) > 0:
            print("Veicoli a 2 ruote:")
            for veicolo in self.v2ruote:
                print(veicolo.nome, veicolo.lunghezza)

        if len(self.v4ruote) > 0:
            print("Veicoli a 4 ruote:")
            for veicolo in self.v4ruote:
                print(veicolo.nome, veicolo.peso, veicolo.num_posti)

    def cancellaVeicolo(self, nome):

        for veicolo in self.v2ruote:
            if veicolo.nome == nome:
                self.v2ruote.remove(veicolo)

        for veicolo in self.v4ruote:
            if veicolo.nome == nome:
                self.v4ruote.remove(veicolo)

    def getNumeroDiRuotePresenti(self):
        ruote = 0
        for veicolo in self.v2ruote:
            ruote += 2

        for veicolo in self.v4ruote:
            ruote += 4
        
        print("Ruote totali: ", ruote)


class veicolo2Ruote(parcoVeicoli):

    def __init__(self, nome, lunghezza):
        self.nome = nome
        self.lunghezza = lunghezza
    


class veicolo4Ruote(parcoVeicoli):
    def __init__(self, nome, peso, num_posti):
        self.nome = nome
        self.peso = peso
        self.num_posti = num_posti



p = parcoVeicoli()
v2 = veicolo2Ruote("moto", 22.4)
v4 = veicolo4Ruote("auto", 150, 5)

p.add2Ruote(v2)
p.add4Ruote(v4)

p.getContenuto()

p.cancellaVeicolo("moto")

p.getContenuto()

p.getNumeroDiRuotePresenti()