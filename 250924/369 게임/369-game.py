N = int(input())



for i in range(1,N+1):
    a = str(i)

    if (i%3==0) or ('3' in a) or ('6' in a) or ('9' in a):
        print(0 , end=" ")
    else :
        print(i , end=" ")