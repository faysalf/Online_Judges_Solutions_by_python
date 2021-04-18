def prime(a,b):
    li = [False if x%2 == 0 else True for x in range(100002)]
    li[1],li[2] = False, True
    for i in range(3,int(100002**0.5),2):
        for j in range(i*i,100002,i): li[j] = False
    count = 0
    for i in range(a,b+1):
        if li[i]: count += 1
    print(count)
if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        a,b = map(int,input().split())
        prime(a,b)
