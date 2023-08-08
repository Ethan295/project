import datetime
import locale

class calcolaCompleanno:

    def __init__(self, giorno, mese, anno):
        self.giorno = giorno
        self.mese = mese
        self.anno = anno

    def calcolaGiorniCompleanno(self):
        locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

        for _ in range(10):
            data = datetime.date(self.anno, self.mese, self.giorno)
            giorno_sett = data.strftime("%A")

            print("Nel:" , self.anno, "è", giorno_sett)
            self.anno += 1



c = calcolaCompleanno(12,11,2000)
c.calcolaGiorniCompleanno()

