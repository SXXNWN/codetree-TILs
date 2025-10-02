A , B = map(int,input().split())
C = A
D = 1

if B == 0 :
    print(1)
else :

    for i in range(B):
        if i == 0 :
            A *= D
        else :
            A *= C
    print(A)
   

