N = int(input())
lista = list(map(int , input().split()))
M = int(input())
lista_suma = list(map(int , input().split()))   
suma=0
for i in range(M):
    inicio = 0 
    final = len(lista)-1
    while inicio <= final:
        puntero = (inicio + final)//2
        if lista_suma[i] == lista[puntero]:
            suma += puntero+1
           
            break
            
        elif lista_suma[i] > lista[puntero]:
            inicio = puntero + 1
            
        else: 
            final = puntero - 1
print(suma)
'''Dado un arreglo de números enteros sin valores repetidos y ordenado ascendentemente, supongamos que necesitamos saber cuál es la suma de las posiciones (contando la primer posición como la 1, no como la 0) que en dicho arreglo tienen cierto conjunto de elementos.

Por ejemplo, si el arreglo es  <  2, 4, 6, 8, 10  >  y tenemos los elementos 4, 8, y 12, la suma de las posiciones sería:

El 4 está en la posición 2 del arreglo, entonces suma 2

El 8 está en la posición 4 del arreglo, entonces suma 4

El 12 no está en el arreglo, entonces suma 0

Por tanto suma total  =  2 + 4 + 0  =  6

Input
La entrada comienza con una línea que contiene un valor entero positivo N (1 ≤ N ≤ 200000) que corresponde al tamaño del arreglo. Luego una línea con N valores enteros en el rango [ - 109, 109] separados entre sí por un espacio en blanco. Todos los valores son diferentes y están ordenados ascendentemente. Luego sigue una línea que contiene un valor entero positivo M (1 ≤ M ≤ 10000) que corresponde a la cantidad de elementos de los que se debe sumar las posiciones. Luego sigue una línea con M valores enteros en el rango [ - 109, 109].

Output
La salida debe tener una única línea con el valor de la suma de las posiciones.'''