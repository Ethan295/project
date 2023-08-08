import string
import itertools

tutti_caratteri = string.ascii_letters + string.digits + string.punctuation + " "

password = "12"

trovato = False

for lunghezza in range(1, 6):
    if trovato:
        break
    
    for perm in itertools.product(tutti_caratteri, repeat=lunghezza):
        combinazione = "".join(perm)
        if password in combinazione:
            trovato = True
            print("Trovato:", combinazione)
            break  # Esce solo dal ciclo interno
        else:
            print(combinazione)
    
    if trovato:
        break  # Esce anche dal ciclo esterno

if not trovato:
    print("Password non trovata.")
