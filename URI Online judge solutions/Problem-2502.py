c,n = map(int,input().split())
s = input()
ss = input()
sss = []
for i in range(n):
    S = input()
    for j in range(c):
        S.replace(s[j],ss[j])
        S.replace(ss[j],s[j])
    sss.append(S)
print(sss)

#li[i] = li[i+1]
