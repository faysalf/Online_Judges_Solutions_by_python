N = int(input())
for _ in range(N):
    a,b,c = map(float,input().split())
    average = ((a/10)*2 + (b/10)*3 + (c/10)*5)
    print("%.1f"%average)
