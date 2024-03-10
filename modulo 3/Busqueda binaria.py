lista = [11, 22 , 25 , 5, 89, 55, 33, 16, 32, 44, 66, 89, 64]
lista.sort() #ordenamos la lista


#1ro Buscar el punto medio
#2do Comprobar si el punto medio es el valor que buscamos
#3ro  el número es menor al valor que buscamos aumentamos 1 sobre el puntero
#4to si el numero es mayor al valor que buscamos disminuimos el funal 1 bajo el puntero
#5to si inicio mayor o igual que final entonces el numero no esta en la lista

def busquedabinaria(valor):
    inicio = 0    
    final = len(lista)-1
    while inicio <= final:
        puntero = (inicio + final)//2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else: 
            final = puntero - 1
    return None
print(lista)

def buscar_valor(valor):
    resultado = busquedabinaria(valor)
    if resultado is None:
        return f"El numero {valor} no se encuentra en la lista" 
    else:
        return f"El numero {valor} se encuentra en la posicion {resultado}"
    
print(buscar_valor(32))