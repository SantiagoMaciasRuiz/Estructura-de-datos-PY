C = int(input())

for _ in range(C):
    valores = list(map(int, input().split()))
    valores.sort()
    frecuencia = {}
    for num in valores:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num]=1
    valores_concatenados = " ".join(str(valor) for valor in frecuencia.values())
    print(valores_concatenados)
    
'''Dados N números enteros debes determinar cuántas veces está el menor de todos, cuántas veces el segundo menor, y así sucesivamente hasta cuántas veces el mayor de todos.

¡Simple! ¿O quizá no?

Input
La primera línea de la entrada contiene la cantidad C de casos, no más de 5. Luego siguen C líneas, cada una con N valores enteros (1 ≤ N ≤ 1000000) separados entre sí por un espacio en blanco. Dichos valores serán, en valor absoluto, inferiores a 10000.

Output
La salida debe contener C líneas, con entre 1 y N valores separados entre sí por un espacio en blanco.'''
        
   

