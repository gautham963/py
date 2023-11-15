#This is a HackerRank problem. Takes set as input finds the difference between the sets and gives output as merged ordered output.

def sets(a,b):
    diff1 = list(sorted(a.difference(b)))
    diff2 = list(sorted(b.difference(a)))
    num = []
    for i in range(len(diff1)):
        num.append(diff1[i])
        
    for j in range(len(diff2)):
        num.append(diff2[j])
        
    final = sorted(num)
    for value in range(len(final)):
        print(final[value])

a = set(map(int,input().split()))
b = set(map(int,input().split()))
sets(a,b)
