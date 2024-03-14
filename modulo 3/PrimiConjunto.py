def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
    

C = int(input())
for _ in range(C):
    valores = list(map(int,input().split()))
    lista = list(map(int,input().split()))
    divisores = calcular_divisores(valores[1])
    intervalo = len(divisores)
    for i in divisores:
        if i in lista:
            intervalo = intervalo
        else:
            intervalo -= 1
    if intervalo == len(divisores):
        print("Es PrimiConjunto")
        
    else:
        print("No es PrimiConjunto")
'''Ya todos sabemos que un número primo es aquel número entero mayor o igual a 2 que solo tiene como divisores a sí mismo y a la unidad. Bueno, pues resulta que si C es un conjunto de números enteros positivos, decimos que es PrimiConjunto de P si contiene entre sus elementos a TODOS los divisores de P (que no es lo mismo que decir que todos sus elementos son divisores de P ).

En este punto te estarás preguntando ¿no se debería llamar entonces DiviConjunto? Pues no! Suena mejor PrimiConjunto y no se diga más.

Por ejemplo, A = {1, 2, 4, 6, 8} es un PrimiConjunto de P = 8 pues contiene todos sus divisores, pero no es PrimiConjunto de P = 6 pues no contiene a 3.

Así mismo, B = {1, 3, 15} no es Primiconjunto de P = 15 pues, aunque todos sus elementos son divisores de 15, falta el 5. Entre tanto, si es PrimiConjunto de P = 3 pues contiene todos sus divisores.

Input
La entrada comienza con una línea que contiene la cantidad de casos C (1 ≤ C ≤ 10). Cada caso se compone de dos líneas. La primera contiene dos valores enteros separados entre sí por un espacio en blanco: N, que corresponde a la cantidad de elementos de C, y el valor de P (2 ≤ N ≤ 10000, 1 ≤ P ≤ 500000). La segunda contiene los N elementos de C ordenados ascendentemente y separados entre sí por un espacio en blanco, cada uno en el rango [1, 100000]. Pueden haber repetidos.

Output
La salida debe contener K líneas, cada una con el mensaje "Es PrimiConjunto" o "No es PrimiConjunto" según sea el caso.'''
        
        
        
        
 
        
           

    
    
