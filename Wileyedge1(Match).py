ar=list(map(int,input().split()))
br=list(map(int,input().split()))
ar.sort()
ans=[]
for i in br:
    val = i
    count = 0
    for j in ar:
        if j <= val:
            count += 1
    ans.append(count)
    
print(ans)
