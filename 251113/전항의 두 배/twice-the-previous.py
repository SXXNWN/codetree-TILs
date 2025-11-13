a , b = map(int , input().split())
arr = []
arr.append(a)
arr.append(b)

for i in range(2,10):
    c = arr[i-1]+(2*arr[i-2])
    arr.append(c)

for i in range(0 , 10):
    print(arr[i] , end = " ")