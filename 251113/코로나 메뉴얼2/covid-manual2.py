total_cnt = 0
A_cnt = 0
B_cnt = 0
C_cnt = 0
D_cnt = 0


for i in range(3):
    arr = input().split()

    if arr[0] == 'Y' :
        if int(arr[1]) >= 37 :
            A_cnt += 1
            total_cnt += 1
        else :
            C_cnt += 1
    else :
        if int(arr[1]) >= 37 :
            B_cnt += 1
        else :
            D_cnt += 1


print(A_cnt , B_cnt , C_cnt , D_cnt , sep = " " , end = " ")

if total_cnt >= 2 :
    print('E')

    

