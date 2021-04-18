T = int(input())
A,B,C,D,E = map(int,input().split())
li = [A,B,C,D,E]
res = 0
for i in li:
    if i == T:
        res += 1
print(res)
