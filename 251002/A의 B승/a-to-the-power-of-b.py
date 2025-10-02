A , B = map(int,input().split())
C = A
D = 1

for i in range(B):
    if i == 0 :
        A *= D
    else :
        A *= C
    
   

print(A)