N = int(input())
Y = list(map(int,input().split()))
new = []

for i in range(N) :
    new.append(Y[i]*Y[i])

for i in range(len(new)) :
    print(new[i] , end = " ")


