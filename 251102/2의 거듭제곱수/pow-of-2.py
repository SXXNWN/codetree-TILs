N = int(input())
cnt = 0

while(True):
    if N == 1 :
        print(cnt)
        break
    
    N /= 2
    cnt += 1