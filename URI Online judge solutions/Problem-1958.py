'''
X = float(input())
st = str(int(X))
ln = len(st)
if ln <= 110:
    res = "{:.4E}".format(X)
    if len(res)<=110:
        if st[0] != "-":
            print("+",end="")
        print(res)
'''

from decimal import Decimal
X = input()
if Decimal(X)>=0 and X[0] != "-":
    print("+",end="")
print("%.4E"%Decimal(X))
