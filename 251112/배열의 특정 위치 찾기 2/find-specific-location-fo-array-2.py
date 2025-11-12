arr = list(map(int,input().split()))

sum_a = 0
sum_b = 0

for i in range(10):
    if (i + 1) % 2 != 0 :
        sum_a += arr[i]
    else :
        sum_b += arr[i]

if sum_a >= sum_b :
    print(sum_a-sum_b)
else :
    print(sum_b-sum_a)