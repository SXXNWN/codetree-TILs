cnt = 0
total = 0

while(True):
    N = int(input())
    if N < 20 or N > 29 :
        if(cnt == 0):
            print("0")
        else:
            print(f"{total/cnt:.2f}")
        
        break
    total += N
    cnt += 1


    
