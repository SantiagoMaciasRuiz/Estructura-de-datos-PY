C = int(input())
for i in range(C):
    cantidad= list(map(int,input().split()))
    denominaciones = list(map(int,input().split()))
    denominaciones.sort(reverse=True)
    total = sum(denominaciones)
    print(denominaciones)