class Libro:

    def __init__(self, nome, numPagine):
        self.nome = nome
        self.numPagine = numPagine

    def setNumPagine(self, numPagine):
        self.numPagine = numPagine

    def setNome(self, nome):
        self.nome = nome

    def pageMessage(self):
        print("Numero pagine: ", self.numPagine)


class Vocabolario (Libro):
    def __init__(self, nome, numPagine, numDefinizioni):
        super().__init__(nome, numPagine)
        self.numDefinizioni = numDefinizioni 

    def definitionMessage(self):
        media = self.numDefinizioni / self.numPagine
        print("Numero pagine: ", self.numPagine)
        print("Numero definizioni: ", self.numDefinizioni)
        print("Media definizioni per pagina: ", media)


v = Vocabolario("Il librotto",300,1200)
v.pageMessage()
v.definitionMessage()


"""
Scrivere quindi una classe Vocabolario che estende la classe Libro. La classe deve
contenere una nuova variabile di istanza, numDefinizioni, un costruttore che assegna al
vocabolario un numero di pagine e un numero di definizioni specificati, ed un metodo
definitionMessage() che stampa un messaggio contenente il numero di pagine, il numero
di definizioni ed il numero medio di definizioni per pagina del vocabolario.
Scrivere infine un programma di prova per collaudare le classi e i metodi. 
"""