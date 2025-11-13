a , b = map(int , input().split())
arr = []

while(a > 1):
    a = a // b
    arr.append(a%b)

new_arr = []

for i in range(b):
    cnt = 0 
    for j in arr :
        if j == i :
            cnt += 1
    new_arr.append(cnt*cnt)

print(sum(new_arr))
    
