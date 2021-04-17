#!/bin/python3
'''
import os

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    div = max(x)-min(x) + 1
    result = div/(k*2 +1)
    if int(result)<result:
        result = int(result+1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
n,k = map(int,input().split())
li = list(map(int,input().split()))
div = max(li)- min(li) + 1
result = div/(k*2 +1)
if int(result)<result:
    result = int(result+1)
print(result)
