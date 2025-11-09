n = int(input())
cnt = 65

for i in range(n):
    for i in range(i+1):
        if chr(cnt) == 'Z' :
        
            print((chr(cnt)) , end = "")
            cnt = 65
        else :
            print((chr(cnt)) , end = "")
            cnt += 1
    print()