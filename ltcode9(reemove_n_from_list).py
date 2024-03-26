def removeElement(array,n):
    
    for i in range(len(array)):
        if n in array:
            array.remove(n)

    print(len(array))


array = list(map(int,input().split()))
n = int(input())
removeElement(array,n)
              
