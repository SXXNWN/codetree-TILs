a , b = map(int , input().split())

arr1 = list(map(int , input().split()))
arr2 = list(map(int , input().split()))

new_arr = []
cnt = 0
check = 'No'

for i in range(a):
    if arr1[i] == arr2[0] :
        for j in range(i , len(arr2)+i):
            new_arr.append(arr1[j])
        cnt += 1
    
    if cnt == 1 :
        break
    
        
    
for i in range(len(new_arr)):
    if arr2[i] == new_arr[i]:
        check = 'Yes'
        if i-1 == len(arr2):
            break
    elif arr2[i] != new_arr[i] :
        check = 'No'
        break

print(check)



