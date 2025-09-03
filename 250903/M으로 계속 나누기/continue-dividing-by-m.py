N, M = map(int, input().split())

# Please write your code here.
print(N)

while N != 0 :
    N //= M
    if N!=0:
        print(N)
