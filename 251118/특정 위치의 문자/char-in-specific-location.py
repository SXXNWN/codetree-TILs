arr = ["L" , "E" , "B" , "R" , "O" , "S"]
check = input()

index = -1 

for i in range(len(arr)):
    if arr[i] == check :
        index = i

if index == -1 :
    print("None")
else :
    print(index)