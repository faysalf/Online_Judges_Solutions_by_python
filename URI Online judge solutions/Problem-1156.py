i = 1
j = 3
sum = 1
while (2*i) < 524289:
    while j<=39:
        sum += (j/(2*i))
        j += 2
        i *= 2
print("%.2f"%sum)
