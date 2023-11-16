#HackerRank problem interview preparation kit.
def plusMinus(arr):
    neg_count, pos_count, zero_count = 0,0,0
    for i in range(len(arr)):
        if arr[i] < 0:
            neg_count += 1
        elif arr[i] > 0:
            pos_count += 1
        elif arr[i] == 0:
            zero_count += 1
            
    #return round(pos_count/len(arr),6)
    #return round(neg_count/len(arr),6)
    #return round(zero_count/len(arr),6)
    
    print(round(pos_count/len(arr),6))
    print(round(neg_count/len(arr),6))
    print(round(zero_count/len(arr),6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
