arr = list(map(int , input().split()))
cnt = 0

for i in range(len(arr)) :
    if arr[i] == 0 :
        cnt = i
        break

print(arr[i-1]+arr[i-2]+arr[i-3])


