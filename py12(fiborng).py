f_n = int(input())
s_n = int(input())

n = 0
n1 = 1

fib = []

for i in range(0,s_n):
    n2 = n1 + n
    n = n1
    n1 = n2
    if (n2 > s_n):
        break
    elif (n2 >= f_n):
        fib.append(n2)

print(fib)
        
