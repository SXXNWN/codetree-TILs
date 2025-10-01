A , B = map(int, input().split())
sum = 0
C = 0

if A > B :
    C = B
    B = A
    A = C
    
    

for i in range(A , B+1):
    if i % 5 == 0 :
        sum += i

print(sum)