arr = list(map(int , input().split()))
set_val = 0

for i in range(len(arr)):
    if arr[i] == 0 :
        set_val = i
        break


for i in range(1 , 10):
    cnt = 0
    for j in range(set_val):
        if arr[j]//10 == i :
            cnt += 1
    print(f"{i} - {cnt}")
    