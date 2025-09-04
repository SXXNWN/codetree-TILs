A , B , C = map(int,input().split())

if A >= B :
    if B >= C :
        print(B)
    elif B <= C :
        if A >= C :
            print(C)
        else :
            print(A)
if B >= A :
    if A >= C :
        print(A)
    elif A <= C :
        if B >= C :
            print(C)
        else :
            print(B)