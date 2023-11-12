#This is Leet Code problem number 1342> The objective is to divide a number by 2
#if its even or subtract 1 from the number and repeat these steps until 0 is obtained
#the output should be the amount of steps required to do this.
def Number_of_Steps(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            count += 1
        elif n % 2 != 0:
            n -= 1
            count += 1

    print(count)

n = int(input())
Number_of_Steps(n)
