A , B = map(int,input().split())
C = A

for i in range(B-1):
    A *= C

print(A)