n = int(input())

for i in range(n+1):
    for j in range(i):
        print('*',end = "")
        #print(j,end = "")this will print numbers instead of '*'
    print("")
