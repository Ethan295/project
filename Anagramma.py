parola1 = "ciao"
parola2 = "oicc"

anagramma = False

if len(parola1) == len(parola2):
    for i in range(len(parola1)):
        if parola2.count(parola1[i]) > 0 and parola1.count(parola2[i]) > 0:
            anagramma = True
        else:
            anagramma = False
            break

print("si") if anagramma else print("no")

# Fatto meglio

"""
if len(parola1) == len(parola2) and sorted(parola1) == sorted(parola2):
    print("si")
else:
    print("no")
"""
