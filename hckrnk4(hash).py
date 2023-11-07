#Given an integer,n, and  space-separated integers as input, create a tuple,t,
#of those n integers. Then compute and print the result of hash(t).

if __name__ == '__main__':
    n = int(input())
    l = ()
    y = list(l)
    integer_list = map(int, input().split())
    y.append(integer_list)
    l = tuple(y)
    print(hash(l))
