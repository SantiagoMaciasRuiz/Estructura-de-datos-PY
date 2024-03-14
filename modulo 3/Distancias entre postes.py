def busquedabinaria(valor,lista):
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
K = int(input())
posicion_postes = list(sorted(map(int,input().split())))
P = int(input())
for i in range(P):
    a , b = map(int,input().split())
    posicion1 = busquedabinaria(a,posicion_postes)
    posicion2 = busquedabinaria(b,posicion_postes)
    print(f"{max(posicion1,posicion2)-min(posicion1,posicion2)} kms")
'''Distancias entre postes
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
El gobierno ha decidido construir una autopista para conectar una región apartada del país. Para ello, va a ser necesario instalar postes de iluminación. La planeación para su ubicación es bastante simple: el primer poste se pondrá al inicio de la autopista, el segundo en el kilómetro 1, el tercero en el kilómetro 2 y así sucesivamente hasta cubrir los K kilómetros que tiene en total la autopista (en total se requieren K + 1 postes). Cada poste está identificado con un código numérico único. Como el ingeniero a cargo de la obra es algo psico-rígido ha decidido que el primer poste sea el de menor código, el segundo poste sea el de segundo menor código, y así sucesivamente hasta que el poste en el extremo final de la autopista sea el de mayor código de todos.

El director de la empresa encargada de proveer los postes quiere saber, por alguna razón desconocida, a que distancia en kilómetros quedaron separados ciertos pares de postes, ¿podrías ayudarle a darle respuesta a sus interrogantes?

Input
La entrada comienza con una línea que contiene un valor entero positivo K inferior a 200000 que corresponde al tamaño de la autopista en kilómetros. Luego sigue una línea que contiene K + 1 valores enteros en el rango [1, 200000], separados entre sí por un espacio en blanco y que corresponden a los códigos de los postes instalados. Dichos valores son únicos pero no están necesariamente ordenados. Luego sigue una línea que contiene un valor entero positivo P (1 ≤ P ≤ 10000) que corresponde a la cantidad de parejas de postes de los cuales se desea conocer la distancia. Luego siguen P líneas, cada una con dos valores enteros en el rango [1, 200000] y separados entre sí por un espacio en blanco. Dichos valores corresponden a códigos de postes válidos.

Output
La salida debe tener P líneas, cada una con el mensaje "x kilometros" (sin comillas ni puntuación), donde x es la distancia entre el par de postes correspondiente.'''
            
    