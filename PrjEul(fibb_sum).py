#ProjectEuler number 2(Sum of evn fibonacci number)
resultant = 0
initial_number = 0
nxt_number = 1
fib = []
evn_fib = []
while nxt_number < 4000000:
    resultant = nxt_number + initial_number
    fib.append(resultant)
    initial_number = nxt_number
    nxt_number = resultant
    
fib.pop()
for i in range(len(fib)):
    if fib[i]%2==0:
        evn_fib.append(fib[i])
    else:
        continue
    
print(fib)
print(evn_fib)
print(sum(evn_fib))
