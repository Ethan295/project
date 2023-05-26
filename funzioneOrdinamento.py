
def ordinamento(lista):
    listaOrdinata = []
    minimo = lista[0]
    while len(lista) > 0:
        for x in range(len(lista)):
            if lista[x] < minimo:
                minimo = lista[x]
        listaOrdinata.append(minimo)
         
        lista.remove(minimo)
        if len(lista) > 0:
            minimo = lista[0]
    print(listaOrdinata)      


lista = [1, 34, 6, 213, 7, 976]
ordinamento(lista)

