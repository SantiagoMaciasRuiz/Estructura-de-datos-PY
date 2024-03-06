N= int(input())
secuencia = list(map(int, input().split()))
acumulados=[] 
for k in range(2,N+1):
    acumuladosK= sum(secuencia[-k:])
    acumulados.append(acumuladosK)

for acumulado in acumulados:
    print(acumulado)

'''Dada una secuencia de N números enteros, necesitamos saber cuál es el acumulado (sumatoria) de los k últimos, con k desde 2 hasta N.

Input
La entrada comienza con una línea que contiene un valor entero positivo N tal que (1≤N≤5000). Luego sigue una línea con N valores enteros, cada uno no en el intervalo [ - 100, 100], separados entre sí por un espacio en blanco.

Output
La salida debe contener N-1 líneas con los acumulados correspondientes.'''