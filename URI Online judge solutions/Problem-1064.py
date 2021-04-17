count = 0
average = 0
a = float(input())
if a>0:
    count+=1
    average += a
b = float(input())
if b>0:
    count+=1
    average += b
c = float(input())
if c>0:
    count+=1
    average += c
d = float(input())
if d>0:
    count+=1
    average += d
e = float(input())
if e>0:
    count+=1
    average += e
f = float(input())
if f>0:
    count+=1
    average += f
print("%d valores positivos"%count)
print("%.1f"%(average/count))
