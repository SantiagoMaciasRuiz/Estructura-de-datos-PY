N = int(input())
palabras = list(map(str,input().split(", ")))
palabra_nueva=[]

for i in range(int(N//2)):
    palabra_nueva.append(palabras[i])
    palabra_nueva.append(palabras[N-i-1])
    
    
for _ in palabra_nueva:
    cadena= "".join(_)
    print(cadena, end="")