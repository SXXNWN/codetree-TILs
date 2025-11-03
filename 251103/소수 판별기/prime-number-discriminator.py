N = int(input())
check = True

for i in range(2 , N):
    if N % i == 0 :
        check = False

if check == True :
    print("P")
else :
    print("C")
