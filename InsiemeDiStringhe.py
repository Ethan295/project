
class InsiemeDiStringhe:

    def __init__(self,*stringa):
        self.stringa = stringa

    def to_string(self):
        print(self.stringa)

    def stringa_lunga(self):
        max = 0
        index = 0
        i = 0
        for x in self.stringa:
            if len(x) > max:
                max = len(x)
                index = i
            i += 1 
        print(f"Stringa più lunga: {self.stringa[index]} con {max} caratteri")

    def spazi_stringa(self):
        max = 0
        index = 0
        i = 0
        for x in self.stringa:
            if x.count(" ") > max:
                max = x.count(" ")
                index = i
            i += 1 
        print("Stringa con più spazi: " + self.stringa[index] + " con " + str(max) + " spazi")

    def pre_stringa(self,inizio):
        for x in self.stringa:
            if x.startswith(inizio):
                print("La stringa: " + x + " inizia con " + inizio) 




i = InsiemeDiStringhe("ci a oa","ppp ppp p","a aaa aa a")
i.to_string()
i.stringa_lunga()
i.spazi_stringa()
i.pre_stringa("a aa")

