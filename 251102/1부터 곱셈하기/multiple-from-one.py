N = int(input())

cnt = 1

for i in range(1,11):
    cnt *= i
    if (cnt >= N):
        print(i)
        break