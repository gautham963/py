#This program checks if a number can be sum of two prime numbers.

number = int (input('Enter the number: '))

arr = []

for i in range(2,number):
    flag = 0
    for j in range(2,i):
        if i%j == 0:
            flag = 1

    if flag == 0:
        arr.append(i)


flag = 0
l = len(arr)
for i in range(l):
    for j in range(i+1,l):
        if arr[i] + arr[j] == number:
            flag = 1
            print("The numbers are "+str(arr[i])+" and "+str(arr[j])+" for:"+str(number))


if flag == 0:
    print("No numbers")
        
    
