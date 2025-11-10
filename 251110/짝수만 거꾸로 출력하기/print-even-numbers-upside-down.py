n = int(input())
arr = list(map(int, input().split()))
new_arr = []
cnt = 0

for i in arr:
    if i % 2 == 0 :
        new_arr.append(i)
        cnt += 1
    
    else :
        continue

for i in range(cnt-1 , -1 , -1):
    print(new_arr[i] , end = " ")




    