A, B = input().split()
AB = int(A) + int(B)
Array = [input() for i in range(AB)]

Aarray = Array[:int(A)]
Barray = Array[int(A):]

super_index = []

for bval in Barray:
    IND = []
    Aarray_copy = Aarray[:]
    
    for i in range(len(Aarray_copy)):
        if bval in Aarray_copy:
            index = Aarray_copy.index(bval)
            IND.append(index + 1)
            Aarray_copy[index] = '#'
        else:
            break
    
    if IND:
        super_index.append(IND)
    else:
        super_index.append([-1])

for ele in super_index:
    print(*ele)
