def repeating_elements(arr, n):

    visited = [False for i in range(n)]
    already_printed = []

    for i in range(n):

        if visited[i] or arr[i] in already_printed:
            continue

        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1

        if count > 1:
            print(arr[i])
            already_printed.append(arr[i])

arr = [int(x) for x in input().strip().split()]

n = len(arr)
repeating_elements(arr, n)
