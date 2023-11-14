#LeetCode problem 13, converts Roman numerals to Integers.
s = input()
Roman_numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total = 0
for i in range(len(s)-1):
    if Roman_numerals[s[i]] < Roman_numerals[s[i+1]]:
        total -= Roman_numerals[s[i]]
    else:
        total += Roman_numerals[s[i]]

        
print(total + Roman_numerals[s[-1]])
