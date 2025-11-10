arr = list(map(int , input().split()))
new_arr = []
cnt = 0

for i in arr :
    if i == 0 :
        break
    new_arr.append(i)
    cnt += 1


for j in range(cnt-1 , -1 , -1):
    print(new_arr[j] , end = " ")