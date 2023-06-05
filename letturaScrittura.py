import re

input = open("input.txt", "r")
output = open("output.txt", "w")

output.truncate()

vocali = "aeiouAEIOU"

testo_modificato = ""

for riga in input.readlines():
    
    parole = riga.split(" ")

    for parola in parole:

        testo_modificato = ""
        for carattere in parola:
            if not carattere == " ":
                if carattere.islower():
                        testo_modificato += carattere.upper() + " " 
                else: 
                        testo_modificato += carattere.lower() + " " 
                

        testo_modificato = testo_modificato.translate(str.maketrans("", "", vocali))
        testo_modificato = re.sub(r' +', ' ', testo_modificato)

        output.write(testo_modificato[::-1])


input.close()
output.close()