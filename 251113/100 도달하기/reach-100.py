n = int(input())

arr = []
arr.append(1)
arr.append(n)
cnt = 2

print(arr[0] , arr[1] , sep = " " , end = " ")

while(True):
    a = arr[cnt-2] + arr[cnt-1]
    arr.append(a)
    print(a , end = " ")

    if a >= 100 :
        break
    else :
        cnt += 1