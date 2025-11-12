arr = list(map(int , input().split()))
sum_even = 0
sum_3 = 0
cnt = 0

for i in range(10):
    if i % 2 != 0 :
        sum_even += arr[i]

for i in range(10):
    if (i+1) % 3 == 0 :
        sum_3 += arr[i]
        cnt += 1

print(sum_even , sum_3/cnt , sep = " ") 
