elements = list(map(int,input().split()))
l = len(elements)
Sum = []

for i in range(0,l):
    if i+1 < l:
        ele1 = elements[i]
        ele2 = elements[i+1]
        sm = ele1 + ele2
        print('The sum is {} for the elements {} and {}'.format(sm,ele1,ele2)) 
        Sum.append(sm)
    else:        
        break

print(Sum)
        
