P,N = map(int,input().split())
li = list(map(int,input().split()))
a = 1

while a<N:
    if abs(li[a]-li[a-1]) > P:
        print("GAME OVER")
        break
    a += 1
else:
    print("YOU WIN")


'''
P,N = map(int,input().split())
li = list(map(int,input().split()))
for i in range(1,P+1):
    if (li[i]-li[i-1]) > P:
        print("GAME OVER")
        break
else:
    print("YOU WIN")
'''
