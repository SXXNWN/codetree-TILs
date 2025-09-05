cnt3 = 0
cnt5 = 0
arr = []

for i in range(1 , 11):
    a = int(input())
    arr.append(a)

for i in arr :
    if i%3 == 0 and i%5 == 0 :
        cnt3 += 1
        cnt5 += 1
        continue

    elif i%3 == 0 :
        cnt3 += 1
    elif i%5 == 0 :
        cnt5 += 1

print(cnt3, cnt5 , sep = " ")

