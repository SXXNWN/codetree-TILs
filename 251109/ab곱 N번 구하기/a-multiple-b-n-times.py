n = int(input())
y = 1

for i in range(n):
    arr = input().split()
    a , b = int(arr[0]) , int(arr[1])
    for j in range(a , b+1):
        y *= j
    print(y)
    y = 1