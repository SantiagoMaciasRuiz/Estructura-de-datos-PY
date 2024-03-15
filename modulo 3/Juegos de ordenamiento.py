C = int(input())
for _ in range(C):
    numeros = list(map(int,input().split()))
    cambios = 0
    for i in range(len(numeros)):
        for j in range(len(numeros)-i-1):
            if numeros[j] > numeros[j+1]:
                cambios+=1
                temp = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = temp
    print(cambios)
                
'''Las directivas de una universidad decidieron que durante el proceso de inducción de los estudiantes era necesario que, de una manera lúdica, comenzaran a familiarizarse con problemas básicos de computación, siendo el ordenamiento uno de ellos. Por eso se inventaron los "juegos de ordenamiento" que consisten en armar equipos y ordenarlos según el documento de identidad.

Para ello cada equipo inicia formando (sin ningún orden en particular) todos sus integrantes en una línea recta. A partir de allí, y realizando únicamente de a un intercambio de dos estudiantes consecutivos, deben ordenarse de menor a mayor. El equipo que termine primero gana, por esta razón es de suma importancia minimizar la cantidad de intercambios.

Input
La primera línea de la entrada contiene la cantidad C de casos, no más de 10. Luego siguen C líneas, cada una con los documentos de identidad de los N de estudiantes de un equipo (1 ≤ N ≤ 1000) separados entre sí por un espacio en blanco según su alineación inicial. Cada documento es único y corresponde a un valor entero positivo inferior a 9999999.

Output
La salida debe contener C líneas, cada una con la correspondiente cantidad mínima de intercambios necesarios para ordenar los N estudiantes de manera ascendente.'''