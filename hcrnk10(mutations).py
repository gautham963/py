def mutate_string(s, i, c):
    l = list(s)
    l[i] = c
    s = ''.join(l)
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
