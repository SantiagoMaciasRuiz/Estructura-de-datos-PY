C = int(input())  
 
for _ in range(C):
    m, n = map(int, input().split())
    personas = [0 for _ in range(m)]
    monedas = list(map(int, input().split()))
    for i in range(n):
        personas[i % m] += monedas[i] #
        
    maximo_recibido = max(personas)
    minimo_recibido = min(personas)
    diferencia = maximo_recibido - minimo_recibido
    
    print(diferencia)

'''Alonso y sus amigos se ganan la vida haciendo presentaciones a los transeúntes en los semáforos de la ciudad. A veces hacen malabares, a veces baile y a veces incluso un poco de magia. Sus espectáculos, aunque breves, gustan mucho por lo que suelen recoger una buena cantidad de dinero. Lo curioso es que a la hora de repartirlo son bastante excéntricos: lo dejan al azar. Más específicamente lo que hacen es que al terminar una jornada juntan todos los billetes y monedas en una enorme pila sin ningún orden en particular (por cuestiones físicas los billetes deben ir en la base de la pila pero, en el fondo, esto no tiene importancia). Luego cada integrante va sacando de a una única moneda o billete en la cima de la pila hasta que esta quede vacía.

Claramente todos reciben aproximadamente la misma cantidad de monedas o billetes, pero no necesariamente el mismo monto total. Lo que ellos dicen y que estadísticamente es correcto, es que, dada la aleatoriedad en la pila y a que cada día varían también de manera aleatoria el orden en que se acomodan los integrantes a la hora de repartir, quien un día obtiene menos en otro obtiene más, entonces a la larga todos obtienen prácticamente lo mismo.

Input
La entrada comienza con una línea que contiene un valor entero positivo C que corresponde a los casos de prueba, no más de 10. Cada caso de prueba comienza con una línea que contiene dos valores enteros positivos separados por un espacio en blanco: la cantidad M de integrantes y la cantidad N de monedas o billetes recolectados (2≤M≤50, 1≤N≤5000). Posterior a esa sigue otra línea con las denominaciones de las N monedas o billetes separadas entre sí por un espacio en blanco. Esas denominaciones no corresponden necesariamente a un sistema monetario específico, solo se tratan de valores enteros positivos inferiores a 10000.

Output
Por cada caso de prueba la salida debe contener una línea con la diferencia entre lo que recibe en total quien recibe más y lo que recibe quien recibe menos.'''