n = int(input())
cnt = 0

for i in range(n , 0 , -1):
    for j in range(n-i):
        print(" " , end = " ")
   
    for j in range(i):
        if chr(ord('A')+cnt) == "Z" :
            print(chr(ord('A')+cnt) , end = " ")
            cnt = 0
            
        else :
            print(chr(ord('A')+cnt) , end = " ")
            cnt += 1
    print()
