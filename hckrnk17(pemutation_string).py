#Hackerrank problem
from itertools import permutations
word,n = input().split()


pemut = list(sorted(permutations(word,int(n))))

output = ''
for pair in pemut:
    output += ''.join(pair)+'\n'
    
print(output)
