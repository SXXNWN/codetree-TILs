n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

min_val = a[0]
min_val_cnt = 0

for i in range(n):
    if a[i] <= min_val :
        min_val = a[i]

for i in range(n):
    if a[i] == min_val :
        min_val_cnt += 1

print(min_val ,min_val_cnt , sep = " ")