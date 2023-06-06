import json


class Prodotto:
    lista_prodotti = []

    def __init__(self):
        self.lista_prodotti = []

    def inserimento(self, lista):
        self.lista_prodotti = lista

    def scrivi_file(self):
        try:
            with open('Prodotti.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.extend(self.lista_prodotti)

        with open('Prodotti.json', 'w') as file:
            json.dump(data, file, indent=4)

    def leggi_file(self):
        with open('Prodotti.json', 'r') as file:
            data = json.load(file)

        nomi_prodotti = [prodotto['nome'] for prodotto in data]

        for nome in nomi_prodotti:
            print(nome)


lista_prodotti = []

for x in range(3):
    nome_prodotto = input("Inserisi il nome del prodotto numero %d: "% (x+1)) 
    prezzo_prodotto = input("Inserisi il prezzo del prodotto numero %d: "% (x+1))
    quantita_prodotto = input("Inserisi la quantita del prodotto numero %d: "% (x+1))
    lista_prodotti.append({"nome": nome_prodotto, "prezzo": prezzo_prodotto, "quantita": quantita_prodotto})

p = Prodotto() 
p.inserimento(lista_prodotti)
p.scrivi_file()
p.leggi_file()




