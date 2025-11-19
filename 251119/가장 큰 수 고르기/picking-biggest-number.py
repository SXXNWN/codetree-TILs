arr = list(map(int , input().split()))
max_val = 0

for i in range(len(arr)):
    if max_val < arr[i]:
        max_val = arr[i]
print(max_val)