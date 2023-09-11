#converting the letters from the 2nd letter into uppercase
String = input()

s = String.split()

for word in s:
    f_l = word[0]
    s_l = word[1:]
    u = s_l.upper()
    U = f_l + u
    print(U)
