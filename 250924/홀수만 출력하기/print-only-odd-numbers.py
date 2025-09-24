N = int(input())
arr = []

for i in range(N):
    num = int(input())
    arr.append(num)

for i in arr:
    if i % 3 == 0 and i % 2 != 0 :
        print(i)

    