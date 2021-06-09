from collections import Counter
test = 1
while True:
    n = int(input())
    if n==0:
        break
    if test != 1:
        print()

    lx = []
    ly = []
    thi,rd = 0, 0
    for i in range(n):
        x,y = map(int,input().split())
        got = y//x
        lx.append(x)
        ly.append(got)

        thi += x
        rd += y

    counter = Counter(ly)   #counter gotten, fx users
    fx = []
    for j in counter:
        f = 0
        for s in range(counter[j]):
            ind = ly.index(j)
            f += lx[ind]
            ly[ind] = None
        fx.append(f)

    li = list(counter)
    sort = sorted(li)
    faka = [0 for i in range(len(li))]

    rt = 0
    for i in sort:
        ind = li.index(i)
        faka[rt] = "%d-%d"%(fx[ind],li[ind])
        rt += 1

    value = int(float("%.2f"%(float(rd)*100)) / thi)
    print("Cidade# %d:"%test)
    print(" ".join(faka),end="")
    print("\nConsumo medio: %.2f m3."%(value/100))
    test += 1