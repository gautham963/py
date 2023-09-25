n = int(input())
factors = []
prime_factor = []

for i in range(2,n):
    if (n%i == 0):
        factors.append(i)
    else:
        continue

print(factors)

for p in factors:
    is_prime = True
    for pf in range(2,p):
        if(p%pf == 0):
            is_prime = False
            break

    if(is_prime == True):
        prime_factor.append(p)

print(prime_factor)
    
