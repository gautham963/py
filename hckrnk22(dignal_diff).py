#Haclerank 1weel preparation kit(diagonal_diff)
n = int(input())
Num = []

for _ in range(n):
    nums = list(map(int,input().split()))
    Num.append(nums)
#print(Num)
#print(len(Num))
    
Sum,Sum1 = 0,0
for i in range(len(Num)):
    Sum += Num[i][i]
    Sum1 += Num[i][(len(Num))-i-1]
    
Absolute_diff = abs(Sum - Sum1)
print(Sum)
print(Sum1)
print(Absolute_diff)
