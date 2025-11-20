n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

max_val = a[0]
check = 0
check_j = 0
check_x = 0

for i in range(n):
    if max_val <= a[i] :
        max_val = a[i]

for i in range(n):
    if max_val == a[i] :
        check = i
        break


for j in range(0 , check):
    if check_j <= a[j]:
        check_j = a[j]

for x in range(check+1 , n):
    if check_x <= a[x]:
        check_x = a[x]

print(max_val , end = " ")

if check_j >= check_x :
    print(check_j)
else :
    print(check_x)
