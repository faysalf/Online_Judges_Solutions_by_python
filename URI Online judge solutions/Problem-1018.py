N = int(input())
print(N)
if N>= 100:
    h = N//100
    print("%d nota(s) de R$ 100,00"%h)
else:
    print("0 nota(s) de R$ 100,00")
S = N%100
if S>= 50:
    f = S//50
    print("%d nota(s) de R$ 50,00"%f)
else:
    print("0 nota(s) de R$ 50,00")
F = S%50
if F>= 20:
    t = F//20
    print("%d nota(s) de R$ 20,00"%t)
else:
    print("0 nota(s) de R$ 20,00")
A = F%20
if A>= 10:
    te = A//10
    print("%d nota(s) de R$ 10,00"%te)
else:
    print("0 nota(s) de R$ 10,00")
Y = A%10
if Y>= 5:
    fi = Y//5
    print("%d nota(s) de R$ 5,00"%fi)
else:
    print("0 nota(s) de R$ 5,00")
L = Y%5
if L>= 2:
    tw = L//2
    print("%d nota(s) de R$ 2,00"%tw)
else:
    print("0 nota(s) de R$ 2,00")
M = L%2
if M >= 1:
    o = M//1
    print("%d nota(s) de R$ 1,00"%o)
else:
    print("0 nota(s) de R$ 1,00")
