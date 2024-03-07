C = int(input())
codigo =[]
for i in range(C):
    encri = list(input().split())
    codigo.append(encri)
for palabras in codigo:
    for i in range(len(palabras)//2):
        palabras[i], palabras[-i-1] = palabras[-i-1],palabras[i] 
    for indice in range(1, len(palabras), 2):
        palabras[indice], palabras[indice - 1] = palabras[indice - 1], palabras[indice]
for _ in codigo:
    cadena= "". join(map(str,_))
    print(cadena)
'''La serie televisiva de los 60's Get Smart, traducida en Latinoamérica como Super agente 86 era una parodia de las películas de espías protagonizada por Don Adams, como Maxwell Smart o el agente 86, y Barbara Feldon, como la agente 99.

En la serie había dos agencias de espionaje y contraespionaje: por un lado CONTROL donde estaban 86 y 99, que imitaba a la CIA estadounidense, y por otro KAOs, que imitaba la KGB soviética.

Obviamente el trabajo de ambas agencias era mantener sus secretos y develar los de su contraparte por lo que supongamos que una de ellas usaba el siguiente mecanismo para encriptar mensajes. Considerando únicamente las letras a - z en minúsculas, más los dígitos 0 - 9, más el guion bajo para representar el espacio en blanco, un mensaje M pasa por dos procesos:

M se transforma en M* intercambiando cada carácter en posición impar por el carácter inmediatamente posterior
M *  se transforma en M *  *  intercambiando cada carácter por su imagen especular. Esto es, el carácter en la primera posición se intercambia por el de la última, el de la segunda por el de la penúltima y así sucesivamente.

Por ejemplo para M = "h o l a _ m u n d o"

M* sería = "o h a l m _ n u o d"
M** sería = "d o u n _ m l a h o"
Dada una serie de mensajes encriptados en este sistema, ¿harías un programa para desencriptarlos?

Input
La entrada comienza con una línea que contiene un valor entero positivo C que corresponde a los casos de prueba, no más de 50. Luego siguen C líneas para cada caso, cada una con hasta 2000 caracteres separados entre sí por un espacio en blanco.

Output
Por cada caso de prueba la salida debe contener una línea con el mensaje correspondiente desencriptado sin espacios en blanco.'''