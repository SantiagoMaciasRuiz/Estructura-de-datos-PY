C = int(input())
for _ in range(C):
    valores = list(map(int,input().split()))
    lista = list(map(int,input().split()))
    primos = []
    for i in range (valores[1]):
        if valores[1] % lista[i] == 0:
            num=lista[i]
            primos.append(num)
        
           

    
    
