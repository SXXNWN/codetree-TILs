N = int(input())

for i in range(N , 0 , -1):
    for j in range(N-i):
        print(" " , end = " ")
    
    for z in range(i*2-1):
        print("* " , end = "")
    print()
        

