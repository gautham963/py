t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    n1,n2 = 0,1
    
    fib = []
    for i in range(2,n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if (n3 < n) and (n3%2 == 0):
            fib.append(n3)

        Sum = 0
        for value in fib:
            Sum += value
    print(Sum)
    continue
        
