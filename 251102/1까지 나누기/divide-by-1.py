N = int(input())

cnt = N
cnt1 = 1

while(True) :
    cnt /= cnt1
    cnt1 += 1
    if (cnt/cnt1 <= 1):
        print(cnt1)
        break
    
    

    