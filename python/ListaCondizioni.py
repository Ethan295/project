import math




input = input("Inserisci una lista di numeri interi separati da virgola: ")

input = input.replace(" ", "")

lista = input.split(",")

listaCondizionata = ""

for i in range(len(lista)):
    lista[i] = int(lista[i])
    if lista[i] % 2 == 0 and lista[i] > 10 and math.isqrt(lista[i]) ** 2 == lista[i]:
        listaCondizionata.append(lista[i]) 
print(listaCondizionata)
