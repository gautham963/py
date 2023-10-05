# this program is used to check for the perfect number

def perfect(Num):
    fact = []
    s = 0
    for i in range(1,Num):
        if Num%i == 0:
            fact.append(i)
        else:
            continue
    print(fact)    
    for f in fact:
        s += f
        print(s)
    if (s == Num):
        print("Perfect Number:",Num)
    else:
        print("not perfect")
        
Num = int(input())
perfect(Num)
