a1 , a2 = input().split()
b1 , b2 = input().split()
c1 , c2 = input().split()

sum = 0

if a1 == 'Y' :
    if int(a2) >= 37 :
        sum += 1 
if b1 == 'Y' :
    if int(b2) >= 37 :
        sum += 1 
if c1 == 'Y' :
    if int(c2) >= 37 :
        sum += 1 

if sum >= 2 :
    print('E')
else :
    print('N')