#LeetCode problem number1 TwoSum problem
Numbers = [2,7,11,15]
target = 9

for i,num1 in enumerate(Numbers):
    for j,num2 in enumerate(Numbers[i+1:]):
        if num1 + num2 == target:
            print([i,i+1+j])
        
