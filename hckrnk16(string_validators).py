#String validators.
s = input()

print(True) if any(c.isalnum()for c in s) else print(False)
print(True)if any(c.isalpha()for c in s) else print(False)
print(True)if any(c.isdigit()for c in s)else print(False)
print(True)if any(c.islower()for c in s)else print(False)
print(True)if any(c.isupper()for c in s)else print(False)
