N= int(input())
contN=0
contP=0
for i in range(N):
    numero = int(input())
    if numero < 0:
        contN -= numero
    else:
        contP += numero
print(f"positivos {contP}, negativos {-contN}")


'''Dada una secuencia de números enteros, ¿cuál será la sumatoria de los positivos, y cuál la de los negativos?

Input
La entrada comienza con una línea que contiene un valor entero positivo N no mayor a mil. Posteriormente siguen N líneas, cada una con un entero dentro del rango [-9999,9999]

Output
Una única línea con el siguiente mensaje: "positivos Q, negativos R" (sin las comillas) y siendo Q y R la sumatoria de números positivos y negativos respectivamente.'''