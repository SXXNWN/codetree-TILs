n = int(input())
n_cnt = 1
cnt = 0

while(cnt != 2) :
    print(n*n_cnt , end = " ")
    if n*n_cnt % 5 == 0 :
        cnt += 1
    n_cnt += 1