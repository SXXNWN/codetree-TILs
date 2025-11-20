n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_val = nums[0]
cnt = 0

for i in range(n):
    if max_val <= nums[i]:
        max_val = nums[i]

for i in range(n):
    if max_val == nums[i] :
        cnt += 1

if cnt >= 2 :
    print(-1)
else :
    print(max_val)