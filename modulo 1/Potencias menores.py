N = int(input())
N_max = int(input())
for i in range(1,100):
    if (N**i<=N_max):
        print(N**i)
        continue
'''Supongamos que queremos conocer todas las potencias enteras positivas del número 2 que sean menores o iguales a 50. Estas serían: 21 = 2, 22 = 4, 23 = 8, 24 = 16, y 25 = 32. O si quisiéramos conocer las del número 3 menores o iguales a 100 serían: 31 = 3, 32 = 9, 33 = 27, y 34 = 81.

Si generalizamos, el problema sería entonces encontrar las potencias enteras positivas del número A que sean menores o iguales a B.

Input
La entrada comienza con una línea que contiene un valor entero positivo A (2≤A≤20). La siguiente línea contiene un valor entero positivo B (A≤B≤9 × 1016).

Output
La salida debe tener, de a una por línea, las potencias correspondientes.'''