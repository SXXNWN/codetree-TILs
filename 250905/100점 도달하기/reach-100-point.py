N = int(input())
arr = []
for i in range(N , 101):
    if i >= 90 :
        arr.append('A')
    elif i >= 80 :
        arr.append('B')
    elif i >= 70 :
        arr.append('C')
    elif i >= 60 :
        arr.append('D')
    elif i < 60 :
        arr.append('F')

for i in range(len(arr)):
    print(arr[i] , end=" ")