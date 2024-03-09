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
    


