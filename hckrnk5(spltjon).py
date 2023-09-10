
def split_and_join(line):
    l = line.split()
    l1 = "-".join(l)
    print(l1)

if __name__=="__main__":
    line = input()
    split_and_join(line)
