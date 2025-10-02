A , B = map(int,input().split())
C = 1

for i in range(1,B+1):
    if i % A == 0 :
        C *= i

print(C)