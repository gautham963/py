#There are some issue in this code due to set appending non-numeric characters 
n = list(map(int,input().split()))

n.sort()
n = str(n)

set_n = set(n)

print(set_n)
list_set = list(set_n)
list_set.sort()
print(list_set)

uniq = []

for i in range(len(list_set)):
    val = list_set[i]
    print(val)
    count = 0
    
    for j in range(len(n)):
        if val == n[int(j)]:
            count += 1
    if count%2 != 0 and val.isdigit():
        print(val)
        #uniq.append(int(val))

#print(sum(uniq))
