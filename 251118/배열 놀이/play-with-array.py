n , q = map(int , input().split())
arr = list(map(int , input().split()))
index = -1

for i in range(q):
    new_arr = list(map(int , input().split()))
    if len(new_arr) <= 2 :
        a = new_arr[0]
        b = new_arr[1]
    else :
        a = new_arr[0]
        b = new_arr[1] 
        c = new_arr[2]

    if a == 1 :
        print(arr[b-1])
    elif a == 2 :
        for j in range(n):
            if arr[j] == b :
                print(j+1)
                index = j
                break
            
    elif a == 3 :
        for x in range(b-1 , c):
            print(arr[x] , end = " ")
        print()
    
