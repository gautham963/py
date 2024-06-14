#HackerRank thing its not accepting even though its proper

# Complete the solve function below.
def solve(s):
    words = s.split()
    tot = []

    for i in range(len(words)):
        word = words[i]
        Char = [char for char in word]
        char1 = Char[0]
        Char.remove(char1)
        char1= char1.upper()
        Char.insert(0,char1)
        new_wrd = "".join(Char)
        tot.append(new_wrd)
        
    final_word = " ".join(tot)
    print(final_word)
    return final_word

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
