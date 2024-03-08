N = int(input())
palabras = list(map(str,input().split(", ")))
palabra_nueva=[]

for i in range(N):
    if i % 2 ==0:
        palabra_nueva.append(palabras[i//2])
    else:
        palabra_nueva.append(palabras[N-(i//2)-1])
    
    
for _ in palabra_nueva:
    cadena= "".join(_)
    print(cadena, end="")

'''Cuando tenemos un arreglo con N elementos y necesitamos recorrerlo por alguna razón, lo más natural es hacerlo de izquierda a derecha, ¿verdad? Esto es, desde el índice 0 hasta el N - 1 aumentando de a uno.

Bueno, pues en un recorrido arcoíris también se pasa por todos los elementos una única vez, pero en un orden bastante peculiar. Como se muestra en la figura, se parte del índice 0, de allí se va para el N - 1, de allí para el 1, de allí se va para el N - 2, de allí para el 2, de allí se va para el N - 3, y así sucesivamente hasta llegar al "centro" del arreglo.


Input
La entrada comienza con una línea que contiene un valor entero positivo N (2≤N≤5000) que corresponde al tamaño del arreglo. Luego sigue una línea con N valores, todos caracteres A - Z, separados entre sí por una coma y un espacio en blanco.

Output
La salida debe contener una única línea con la concatenación de todos los elementos del arreglo siguiendo el recorrido descrito.'''