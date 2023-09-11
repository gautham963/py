n = int(input())

n1 = 0
n2 = 1

fib = [0,1]

for i in range(2,n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

    if n3 > n:
        break
    else:
        fib.append(n3)

print(fib)
    
