N = int(input())
ju_so=list(input().split(","))
ju_lar=list(input().split(","))
ju_is=list(input().split(","))
SO = 'SO'
LAR = 'LAR'
IS = 'IS'
resultados = {SO: 0, LAR: 0, IS: 0}

for i in range(N):
    suma_jugadas = int(ju_so[i]) + int(ju_lar[i]) + int(ju_is[i])
    if suma_jugadas % 2 == 0:
        if(int(ju_so[i])%2 ==0):
            resultados[SO] += 1
        if (int(ju_lar[i])%2 ==0):
            resultados[LAR] += 1
        if (int(ju_is[i])%2 ==0):
            resultados[IS] += 1
    else: 
        if(int(ju_so[i])%2 !=0):
            resultados[SO] += 1
        if (int(ju_lar[i])%2 !=0):
            resultados[LAR] += 1
        if (int(ju_is[i])%2 !=0):
            resultados[IS] += 1

# Imprimir el diccionario en una sola línea
print(f"{SO}:{resultados[SO]}, {LAR}:{resultados[LAR]}, {IS}:{resultados[IS]}")
       
    
'''El problema de los tres cuerpos es una novela de ciencia ficción del escritor chino Liu Cixin que hace parte de la trilogía titulada El recuerdo del pasado de la Tierra donde también están El bosque oscuro y El fin de la muerte.​ El título hace referencia al problema de astrodinámica que consiste en determinar, en cualquier instante, las posiciones y velocidades de tres cuerpos con diferente masa, sometidos a atracción gravitacional mutua y partiendo de unas posiciones y velocidades dadas.

Si ya leíste por lo menos el primer libro, sabrás que los trisolarianos son una raza extraterrestre con muchas particularidades. Una de ellas, presumiblemente, es que les gusta un juego con tres participantes. Por turnos, cada uno elije un valor entero entre uno y ocho (también, presumiblemente, tienen 8 dedos y un sistema numérico octal). Si un jugador elije un valor par, y la suma de los tres valores da par, ese jugador gana un punto. Igual ocurre si elige un valor impar y la suma da impar.

Dada una serie de N turnos, ¿les ayudarías a determinar el puntaje final? Al primer jugador se le denomina SO, al segundo LAR, y al tercero IS.

Input
La entrada comienza con una línea que contiene un valor entero positivo N tal que (1≤N≤12000) que corresponde a la cantidad de turnos. Luego siguen tres líneas, la primera para las N jugadas del jugador SO, la segunda paras las N jugadas del jugador LAR, y la tercera para las N jugadas del jugador IS. En los tres casos los valores se encuentran separados entre sí por una coma y un espacio en blanco.

Output
La salida debe contener una única línea con el mensaje SO:X, LAR:Y, IS:Z con los puntajes correspondientes.'''

