def expo_sum(a,b,c,d):
    first_var = a**b
    second_var = c**d
    
    Sum = first_var + second_var
    
    return Sum
    
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = expo_sum(a,b,c,d)
print(result)
