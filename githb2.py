#Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def my_range(start, end, step):
     while start > end:
        yield start
        start -= step

n = int(input("Enter the number: "))


for x in my_range(n, 0,1):
    x *= (n-1)
    
print(x)
            
             
