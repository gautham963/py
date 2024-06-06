#collections.namedtuple()


def Marks_calculator(n,tab,tab_cont):
    tab = [x.upper() for x in tab]

    if 'MARKS' in tab:
        ind = tab.index('MARKS')

    MARKS = []
    for i in range(n):
        marks = tab_cont[i][ind]
        MARKS.append(marks)

    MARKS = [eval(i) for i in MARKS]
    total = sum(MARKS)

    avg = total/n

    return avg

n = int(input())
tab = list(map(str,input().split()))
tab_cont = [input().split() for c in range(n)]

Marks_calculator = Marks_calculator(n,tab,tab_cont)

print(Marks_calculator)
