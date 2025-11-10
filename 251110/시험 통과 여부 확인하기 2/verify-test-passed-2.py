n = int(input())
pass_cnt = 0

for i in range(n):
    sum_val = 0
    arr = list(map(int , input().split()))

    for j in arr :
        sum_val += j
    
    if sum_val/4 >= 60 :
        print("pass")
        pass_cnt += 1
    else :
        print("fail")

print(pass_cnt)
