def lonely_integer(arr):
    unique = []
    for i in range(len(arr)):
        ele = arr[i]
        if ele not in unique:
            unique.append(ele)
        elif ele in unique:
            unique.remove(ele)
        else:
            continue

    for i in unique:
        print(i)

arr = list(map(int,input().split()))
lonely_integer(arr)
