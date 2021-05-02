def waystopow(X,N,r):
    val = X - r**N
    if val == 0:
        return 1
    elif val < 0:
        return 0
    else:
        return waystopow(val,N,r+1) + waystopow(X,N,r+1)

if __name__=="__main__":
    X = int(input())
    N = int(input())
    print(waystopow(X,N,1))


'''
import os
def powerSum(X, N, extra):
    value = X - pow(extra,N)
    if value == 0:
        return 1
    elif value < 0:
        return 0
    return powerSum(value,N,extra+1) + powerSum(X,N,extra+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N, 1)

    fptr.write(str(result) + '\n')

    fptr.close()


    fptr.write(str(result) + '\n')

    fptr.close()
'''