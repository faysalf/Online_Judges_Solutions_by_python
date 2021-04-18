N,M = map(int,input().split())
result = N
for _ in range(M):
    st = input()
    result -= 1     #jetate likhbe seta bad
    if st == "fechou":
        result += 2 #akta close korle 2ta open hobe
    else:
        continue
print(result)
