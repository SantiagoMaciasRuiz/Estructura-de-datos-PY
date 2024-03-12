lista = [4,3,2,1,5,6,7,8]
for i in range(0,len(lista)):
    minimo= i
    for j in range(i+1,len(lista)):
        if lista[minimo] > lista[j]:
            minimo = j
    temp = lista[i]

    lista[i]= lista[minimo]
    lista[minimo] = temp
print(lista)