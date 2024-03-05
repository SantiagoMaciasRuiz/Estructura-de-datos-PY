N = int(input())
for i in range(N):
    if (i%2 == 0):
        print("Hola mundo")
    else:
        print("Hello world")

'''Ya todos conocemos el ultra famoso "Hola mundo",
 o su versión en inglés "Hello world". 
 ¿Qué tal si hacemos una pequeña variación y complicados el asunto? La idea es que dado un entero positivo N en el rango no mayor a 10000, se alternen esos mensajes: una vez en español, la siguiente en inglés, la siguiente en español, 
y así sucesivamente hasta mostrar N mensajes.'''