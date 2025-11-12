a , b = map(int , input().split())
arr = [0,0,0,0,0,0,0,0,0,0]
arr[0] = a
arr[1] = b

print(arr[0] , arr[1] , sep = " " , end = " ")

for i in range(2 , 10):
    arr[i] = arr[i-1]+arr[i-2]
    
    print(arr[i]%10 , end = " ")

