arr = ["apple" , "banana" , "grape" , "blueberry" , "orange"]
cnt = 0
a = input()

for i in range(len(arr)) :
    if arr[i][2] == a or arr[i][3] == a :
        print(arr[i])
        cnt += 1
        
print(cnt)

    