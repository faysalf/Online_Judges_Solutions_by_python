par = []
impar = []
for i in range(15):
    n = int(input())
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        count = 0
        for j in par:
            print("par[%d] = %d"%(count,j))
            count += 1
        par = []
    if len(impar) == 5:
        count = 0
        for j in impar:
            print("impar[%d] = %d"%(count,j))
            count += 1
        impar = []
if len(impar) > 0:
    count = 0
    for j in impar:
        print("impar[%d] = %d"%(count,j))
        count += 1
if len(par) > 0:
    count = 0
    for j in par:
        print("par[%d] = %d"%(count,j))
        count += 1


'''
#hoyese but not accepted
par = []
impar = []
for i in range(15):
    n = int(input())
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
count = 0
while count < 5:
    print("par[%d] = %d"%(count,par[count]))
    count += 1
ct = 0
while ct<5:
    print("impar[%d] = %d"%(ct,impar[ct]))
    ct += 1
par.insert(par[-1],0)
impar.insert(impar[-1],0)
par = par[5:-1]
impar = impar[5:-1]
for k in range(len(impar)):
    print("impar[%d] = %d"%(k,impar[k]))
for l in range(len(par)):
    print("par[%d] = %d"%(l,par[l]))
'''
