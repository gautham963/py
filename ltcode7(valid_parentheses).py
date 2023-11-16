#LeetCode problem number 20, Valid parentheses

s = input()
checker = []
for c in s:
    if c in '([{':
        checker.append(c)
    elif (s == '[' or s == ']' or s == '{' or s == '}' or s == '(' or s == ')'):
        print(False)
    else:
        if not checker or \
            (c == ')' and checker[-1] != '(') or \
            (c == ']' and checker[-1] != '[') or \
            (c == '}' and checker[-1] != '{'):
            print(False)
        checker.pop()
print(not checker)#this has to be return instead of print
