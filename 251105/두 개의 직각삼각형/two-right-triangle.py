n = int(input())

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    for z in range((n-i)*2):
        print(" ",end="")
    for x in range(i):
        print('*',end="")
    print()