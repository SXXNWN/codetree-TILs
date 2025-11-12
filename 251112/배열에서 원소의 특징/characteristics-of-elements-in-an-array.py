arr = list(map(int , input().split()))

for i in range(len(arr)):
    if arr[i] % 3 == 0 :
        cnt = i
        break

print(arr[cnt-1])