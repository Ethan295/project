
parola = "anna"
palindromo = False

for i in range(0, len(parola)):
    if parola[i] == parola[-i - 1]:
       palindromo = True 
    else:
        palindromo = False

print("si") if palindromo else print("no")


"""
modo migliore

if parola == parola[::-1]: # [::-1] inverte la stringa
    print("si")
else:
    print("no")
"""