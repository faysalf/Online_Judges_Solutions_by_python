count = 0
odd = 0
positive = 0
negative = 0
a = int(input())
if a%2==0:
    count += 1
else:
    odd += 1
if a>=0:
    positive += 1
elif a<0:
    negative += 1
b = int(input())
if b%2==0:
    count += 1
else:
    odd += 1
if b>0:
    positive += 1
elif b<0:
    negative += 1
c = int(input())
if c%2==0:
    count += 1
else:
    odd += 1
if c>0:
    positive += 1
elif c<0:
    negative += 1
d = int(input())
if d%2==0:
    count += 1
else:
    odd += 1
if d>0:
    positive += 1
elif d<0:
    negative += 1
e = int(input())
if e%2==0:
    count += 1
else:
    odd += 1
if e>0:
    positive += 1
elif e<0:
    negative += 1
print("%d valor(es) par(es)"%count)
print("%d valor(es) impar(es)"%odd)
print("%d valor(es) positivo(s)"%positive)
print("%d valor(es) negativo(s)"%negative)









