cantidad_saltos = int(input())
for i in range(cantidad_saltos):
    N = int(input())
    posicion = 0
    tablero = list(map(int,input().split()))
    posiciones_visitadas = set()
    
    while True:
        # Verificar si la posición actual ya ha sido visitada
        if posicion in posiciones_visitadas:  # Indicar que se ha detectado un ciclo
            break
        posiciones_visitadas.add(posicion)
        posicion += tablero[posicion]
         # Verificar si el jugador ha salido del tablero
        if posicion < 0 or posicion >= N:
            # Indicar que el jugador ha salido del tablero
            break
    print(len(posiciones_visitadas))    
    
'''En este popular juego de mesa los jugadores comienzan en la primera casilla del tablero y se turnan para lanzar un dado que les indicará la cantidad de casillas que deben avanzar en sentido ascendente. Si al finalizar un movimiento un jugador cae en una casilla donde comienza una escalera, sube por ella hasta la casilla donde ésta termina. Si, por el contrario, cae en una en donde comienza la cabeza de una serpiente, desciende por ésta hasta la casilla donde finaliza su cola.

En la versión de programadores, el tablero se reemplaza por un arreglo de N números enteros. Iniciando en el primer índice del arreglo, el jugador debe "saltar" tantos índices hacia adelante o hacia atrás dependiendo como sea el valor del arreglo en ese índice (si es positivo hacia adelante o si es negativo hacia atrás). Al llegar a ese índice se repite el proceso sucesivamente hasta que ocurra una de dos cosas: o que se cierre un ciclo (que en algún punto se salte a un índice por el que ya había pasado) o hasta que salte a un índice que esté por fuera del arreglo. Entendiendo este funcionamiento, lo que se requiere es saber cuántos saltos se requieren para que termine el juego.

Input
La entrada comienza con una línea que contiene un valor entero positivo C (1≤C≤100) que corresponde a la cantidad de casos. Cada caso comienza con una línea que contiene un valor entero positivo N (1≤N≤5000) que corresponde al tamaño del tablero, seguido de una línea con N valores enteros no nulos en el rango [ - 100, 100] separados entre sí por un espacio en blanco.

Output
La salida debe contener C líneas, cada una con la cantidad de saltos en cada caso.'''

