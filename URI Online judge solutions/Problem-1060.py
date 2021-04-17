a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
li = [a,b,c,d,e,f]
count = 0
for i in li:
    if i>0:
        count+=1
print("%d valores positivos"%count)
