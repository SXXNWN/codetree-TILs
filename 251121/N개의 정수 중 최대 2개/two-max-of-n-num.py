n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

max_val = a[0]
max_val_2 = 0
check = 0


for i in range(n):
    if max_val <= a[i] :
        max_val = a[i]

for i in range(n):
    if max_val == a[i] :
        check = i
        break

max_val_2_check = False

for i in range(n):
    if i == check :
        continue
    
    if not max_val_2 :
        max_val_2_check , max_val_2 = True , a[i] 
    if max_val_2 <= a[i]:
        max_val_2 = a[i]

print(max_val , max_val_2 , sep = " ")

