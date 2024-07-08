def uni(a,b,c,d):
    B = set(b)
    D = set(d)
    
    Union = B.union(D)
    
    return len(Union)
    
a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))

result = uni(a,b,c,d)

print(result)    
