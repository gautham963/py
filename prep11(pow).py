n, p = input().split()

#result = pow(int(n),int(p))

#print(result)

N = int(n)
P = int(p)
for i in range(1,P):
    N *= int(n)

print(N)
