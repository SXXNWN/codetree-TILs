arr = list(map(int , input().split()))
min_val = arr[0]
max_val = arr[0]
check = 0

for i in range(len(arr)):
    if arr[i] == -999 or arr[i] == 999 :
        check = i
        break

for i in range(check):
    if arr[i] >= max_val :
        max_val = arr[i]
    
    if arr[i] <= min_val :
        min_val = arr[i]

print(max_val , min_val , sep = " ")




