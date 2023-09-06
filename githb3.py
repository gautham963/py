#With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
#such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
d = dict()
n = int(input("Enter the number: "))
if n == 0:
    print("invalid")

#for  i in range(1,n+1):
#   d.append(i)
#   nu = i*i
#   d.append(nu)
#   continue


for  i in range(1,n+1):
    d[i]= i*i
print(d)
        
