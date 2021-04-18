'''
#hoyechhe but wrong answer
C = int(input())
for _ in range(C):
    s = input()
    ln = len(s)
    ln /= 100
    print(ln)
'''
C = int(input())
for _ in range(C):
    s = input()
    ln = len(s)
    if ln<=9:
        print("0.0%d"%ln)
    elif ln>9 and ln<=99:
        print("0.%d"%ln)
    elif ln>=100:
        h = ln/100
        ln = ln % 100
        if ln >= 10:
            print("%d.%d"%(h,ln))
        elif ln <= 9:
            print("%d.0%d"%(h,ln))
