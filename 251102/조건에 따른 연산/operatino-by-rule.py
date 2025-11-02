cnt = 0
N = int(input())

while(True):
    if N >= 1000 :
        print(cnt)
        break
    
    if N % 2 == 0 :
        N = N * 3 + 1
        cnt += 1
    else :
        N = N * 2 + 2
        cnt += 1

