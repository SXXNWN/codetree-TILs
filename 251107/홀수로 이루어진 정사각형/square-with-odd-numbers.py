n = int(input())
cnt = 0

for i in range(n):
    for j in range(1,n+1):
        print(2*j+(9+cnt) , end = " ")
    cnt += 2
    
    print()