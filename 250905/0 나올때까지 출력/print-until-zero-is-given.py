arr = []

while True :
    a = int(input())

    if a != 0 :
        arr.append(a)
    elif a == 0 :
        for i in range(len(arr)):
            print(arr[i])
        break
