import random

class AppMarket:

    listaApplicazioni = []

    def __init__(self):
        self.listaApplicazioni = []

    def addApp(self, app):
        self.listaApplicazioni.append(app)

    def topCinque(self):
        print("Top 5 app con più download:")
        self.listaApplicazioni.sort(key=lambda x: x.download, reverse=True)
        for i, app in enumerate(self.listaApplicazioni, start=1):
            print(i, app.nome)
            if i == 5:
                break

    def topCinqueNonFree(self):
        print("Top 5 app a pagamento con più download:")
        self.listaApplicazioni.sort(key=lambda x: x.download, reverse=True)
        x = 1
        for i, app in enumerate(self.listaApplicazioni, start=1):
            if not app.free:
                print(x, app.nome)
                if i == 5:
                    break
                x += 1

    def topCinquePerCategoria(self):
        categorie = []
        x = 1
        print("Top 5 app con più download per categoria:")
        self.listaApplicazioni.sort(key=lambda x: x.download, reverse=True)
        for i, app in enumerate(self.listaApplicazioni, start=1):
            if app.categoria not in categorie:
                categorie.append(app.categoria)
            

        for y in range(len(categorie)):
            x = 1
            print(categorie[y])
            for i, app in enumerate(self.listaApplicazioni, start=1):
                if app.categoria == categorie[y]:
                    print(x, app.nome)
                    if x == 5:
                        break
                    x += 1

        # for i, app in enumerate(self.listaApplicazioni, start=1):

    def spesaMediaUtente(self):
        for app in self.listaApplicazioni:
            print(app.nome, "spesa media", app.totaleIncassi/app.download)


    def percentualeFree(self):
        counterFree = 0
        for app in self.listaApplicazioni:
            if app.free:
                counterFree += 1
        print("Percentuale free:", counterFree/len(self.listaApplicazioni)*100, "%")

    def cinqueRandom(self):
        numeriUsciti = []
        print("5 app random:")
        
        while True:
            x = random.randint(0, len(self.listaApplicazioni))
            if x not in numeriUsciti:
                print(len(numeriUsciti)+1, self.listaApplicazioni[x].nome)
                numeriUsciti.append(x)
            if len(numeriUsciti) == 5: break

    def numeroUtenti(self):
         utenti = 0
         for app in self.listaApplicazioni:
            utenti += app.utentiAttivi
         print("Utenti totali:", utenti)


class App:
    def __init__(self, nome, download, free, categoria, totaleIncassi, utentiAttivi):
        self.nome = nome
        self.download = download
        self.free = free
        self.categoria = categoria
        self.totaleIncassi = totaleIncassi
        self.utentiAttivi = utentiAttivi


c = AppMarket()


def cose():
    # c.topCinque()
    # c.topCinqueNonFree()
    # c.topCinquePerCategoria()
    #c.spesaMediaUtente()
    #c.percentualeFree()
    c.cinqueRandom()
    c.numeroUtenti()


    pass

"""
• NumeroUtenti: estrae il numero di utenti
"""


a = App("Clash of Clans", 500000000, True, "Strategia", 1000000000, 10000000)
c.addApp(a)

a1 = App("WhatsApp", 5000000000, True, "Strategia", 10000000000, 1000000000)
c.addApp(a1)

a2 = App("Instagram", 1000000000, True, "Strategia", 5000000000, 1000000000)
c.addApp(a2)

a3 = App("Spotify", 500000000, False, "Social", 5000000000, 500000000)
c.addApp(a3)

a4 = App("TikTok", 1000000000, True, "Strategia", 10000000000, 500000000)
c.addApp(a4)

a5 = App("Netflix", 1000000000, False, "Strategia", 10000000000, 200000000)
c.addApp(a5)

a6 = App("Facebook", 5000000000, True, "Strategia", 20000000000, 2000000000)
c.addApp(a6)

a7 = App("Google Maps", 5000000000, True, "Strategia", 5000000000, 1000000000)
c.addApp(a7)

a8 = App("Telegram", 1000000000, True, "Comunicazione", 10000000000, 500000000)
c.addApp(a8)

a9 = App("Snapchat", 1000000000, True, "Social", 5000000000, 500000000)
c.addApp(a9)

a10 = App("YouTube", 5000000000, True,
          "Comunicazione", 20000000000, 2000000000)
c.addApp(a10)

a11 = App("Google Drive", 1000000000, False,
          "Comunicazione", 5000000000, 500000000)
c.addApp(a11)

a12 = App("Shazam", 500000000, True, "Comunicazione", 2000000000, 100000000)
c.addApp(a12)

a13 = App("Pinterest", 1000000000, True,
          "Comunicazione", 5000000000, 500000000)
c.addApp(a13)

a14 = App("LinkedIn", 500000000, True, "Comunicazione", 1000000000, 200000000)
c.addApp(a14)

a15 = App("Uber", 1000000000000000, False,
          "Comunicazione", 5000000000, 1000000000)
c.addApp(a15)


cose()
