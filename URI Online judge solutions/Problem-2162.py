while True:
    N = int(input())
    li = list(map(int,input().split()))
    if N==2 and li[0]==li[1]:
        count = 0
    else:
        count = 1
        for i in range(1,N-1):
            if not ((li[i]>li[i-1] and li[i]>li[i+1]) or (li[i]<li[i-1] and li[i]<li[i+1])):
                count = 0
                break
    print(count)
'''
n = int(input())
h = [int(x) for x in input().split()]
if n == 2 and h[0] == h[1]:
    pico = 0
else:
    pico = 1
    for i in range(1, n-1):
        if not ((h[i] < h[i-1] and h[i] < h[i+1]) or (h[i] > h[i-1] and h[i] > h[i+1])):
            pico = 0
            break
print(pico)
'''
