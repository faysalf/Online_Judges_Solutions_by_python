def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for i in arr:
        if i>0:
            pos += 1
        elif i<0:
            neg += 1
        elif:
            zer += 1
    print("%.6f"%(pos/n))
    print("%.6f"%(neg/n))
    print("%.6f"%(zer/n))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
