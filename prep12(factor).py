def factor(n):
    factor = []
    for num in range(1,n+1):
        if((n%num)==0):
            factor.append(num)

    print(factor)

n = int(input())
factor(n)
