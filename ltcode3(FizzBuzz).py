#Leet Code puzz 416 "FizzBuzz" problem.

def FizzBuzz(n):
    num = []
    for i in range(1,n+1):
        if (i%3 == 0 and i%5 == 0):
            num.append('FizzBuzz')
        elif (i%3 == 0):
            num.append('Fizz')
        elif (i%5 == 0):
            num.append('Buzz')
        else:
            num.append(str(i))


    print(num)

n = int(input())
FizzBuzz(n)
