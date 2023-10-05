import string

frase = "qwertzuiopasdfghjklyxcvbnm"

lettere = list(string.ascii_lowercase)
panagramma = False

for i in range(len(lettere)):
    panagramma = True if frase.count(lettere[i].lower()) > 0 else False
print(panagramma)


"""
fatto meglio 
import string

frase = "qwertzuiopasdfghjklyxcvbnm"

lettere = set(string.ascii_lowercase)-
frase_senza_spazi = frase.replace(" ", "").lower()

panagramma = lettere.issubset(frase_senza_spazi)

print(panagramma)

"""