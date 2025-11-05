n = int(input())

for i in range(0,n):
    for j in range(n-(i+1)):
        print(" " , end = " ")
    for z in range(i*2+1):
        print("*" , end = " ")
    print()