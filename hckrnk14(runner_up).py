#this program is used to get the second lagest number.

n = int(input())
arr = map(int, input().split())
temp = list(set(arr))
temp.sort()
print(temp[-2])
