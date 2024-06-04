#collections.Counter() in Hackerrank


def profis(n,shoe_size,cust,sale):
    Cost = []
    for i in range(len(sale)):
        size = sale[i][0]
        cost = sale[i][1]
        if size in shoe_size:
            Cost.append(cost)
            shoe_size.remove(size)
            
    prf = sum(Cost)
    return prf
    
n = int(input())
shoe_size = list(map(int,input().split()))
cust = int(input())
sale =[list(map(int,input().split())) for x in range(cust)]

profis = profis(n,shoe_size,cust,sale)
print(profis)
