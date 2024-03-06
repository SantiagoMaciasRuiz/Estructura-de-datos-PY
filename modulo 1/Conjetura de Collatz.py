def Collatz(N):
    print(N)
    if N == 1:
        return
    elif N % 2==0:
        N //= 2
    else    :
        N= (N*3)+1
  
    return Collatz(N)
N = int(input())
Collatz(N)

'''La conjetura de Collatz, conocida también como conjetura 3N+1, fue enunciada por el matemático Lothar Collatz en 1937, y a la fecha no se ha resuelto.

Partiendo de la siguiente operación, aplicable a cualquier número entero positivo: Si el número es par, se divide entre 2 Si el número es impar, se multiplica por 3 y se suma 1

Que formalmente, equivale a tener una función:

f(N)=[ si N es par ; 3N+1 si N es impar]

La conjetura indica que para cualquier N, si se repite indefinidamente dicha operación, eventualmente se llegará a un valor de 1.

Por ejemplo, si N = 6, se obtendría la siguiente sucesión: 6, 3, 10, 5, 16, 8, 4, 2, 1

Si N = 13, se obtendría 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

Input
La entrada contiene una línea con un valor entero positivo N no mayor a 1000.

Output
La salida debe tener, de a una por línea, y comenzando por el valor de N los elementos de la sucesión hasta llegar a 1 (creeremos en Collatz y supondremos que siempre será una sucesión finita).'''