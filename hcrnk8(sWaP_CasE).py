def swp_case(s):
    swapped = ""
    for i in s:
        if i.islower():
            swapped += i.upper()
        else:
            swapped += i.lower()
    return swapped
            

if __name__ == '__main__':
    s = input()
    result = swp_case(s)
    print(result)
