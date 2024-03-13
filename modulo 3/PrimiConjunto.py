def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
    

C = int(input())
for _ in range(C):
    valores = list(map(int,input().split()))
    lista = list(map(int,input().split()))
    divisores = calcular_divisores(valores[1])
    intervalo = len(divisores)
    for i in divisores:
        if i in lista:
            intervalo = intervalo
        else:
            intervalo -= 1
    if intervalo == len(divisores):
        print("Es PrimiConjunto")
        
    else:
        print("No es PrimiConjunto")
 
        
        
        
        
 
        
           

    
    
