N = int(input())
r = ""
s = ""
t = ""
m = N%10
if m==1:
    r += "I"
elif m == 2:
    r += "II"
elif m == 3:
    r += "III"
elif m == 4:
    r += "IV"
elif m == 5:
    r += "V"
elif m == 6:
    r += "VI"
elif m == 7:
    r += "VII"
elif m == 8:
    r += "VIII"
elif m == 9:
    r += "IX"

N = N //10
m = N%10
if m==1:
    s += "X"
elif m == 2:
    s += "XX"
elif m == 3:
    s += "XXX"
elif m == 4:
    s += "XL"
elif m == 5:
    s += "L"
elif m == 6:
    s += "LX"
elif m == 7:
    s += "LXX"
elif m == 8:
    s += "LXXX"
elif m == 9:
    s += "XC"

N = N//10
m = N%10
if m==1:
    t += "C"
elif m == 2:
    t += "CC"
elif m == 3:
    t += "CCC"
elif m == 4:
    t += "CD"
elif m == 5:
    t += "D"
elif m == 6:
    t += "DC"
elif m == 7:
    t += "DCC"
elif m == 8:
    t += "DCCC"
elif m == 9:
    t += "CM"

print(t+s+r)






