check = True

for i in range(5):
    a = int(input())
    if a % 3 != 0 :
        check = False

if check == True :
    print(1)
else :
    print(0)