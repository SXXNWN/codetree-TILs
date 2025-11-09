start, end = map(int, input().split())

# Please write your code here.
add = 0
cnt = 0

for i in range(start , end + 1):
    for j in range(1 , i):
        if i % j == 0 :
            add += j
    if add == i :
        cnt += 1

print(cnt)