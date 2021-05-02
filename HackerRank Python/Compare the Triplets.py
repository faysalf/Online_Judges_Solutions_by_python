import os
import sys
def compareTriplets(a, b):
    alise = 0
    bob = 0
    for i in range(0,3):
        if a[i]>b[i]:
            alise += 1
        elif a[i]<b[i]:
            bob += 1
        else:
            continue
    return [alise, bob]

if __name__ == '__main__':
    #os.environ["OUTPUT_PATH"] = 'junk.txt'
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
