a = list(map(str , input().split()))

reverse =[]

for i in range(-1 , -(len(a)+1) , -1) :
    reverse.append(a[i])

for i in range(10) :
    print(reverse[i] , end="")
