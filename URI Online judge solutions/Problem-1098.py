I = 0
a = 1
b = 2
c = 3
temp = 0
while I<=2:
    if temp == 0:
        print("I=%.0f J=%.0f"%(I,a))
        print("I=%.0f J=%.0f"%(I,b))
        print("I=%.0f J=%.0f"%(I,c))
    else:
        print("I=%.1f J=%.1f"%(I,a))
        print("I=%.1f J=%.1f"%(I,b))
        print("I=%.1f J=%.1f"%(I,c))
    temp += 1
    if temp == 5:
        temp = 0
    I += 0.2
    a += 0.2
    b += 0.2
    c += 0.2


'''
i = 0
j = 1
value = 0
temp = 0
temp2 = 0
while (i <= 2):
    if (temp2 == 0):
        print("I=%.0f J=%.0f" % (i, j))
    else:
        print("I=%.1f J=%.1f" % (i, j))

    temp += 1
    if (temp == 3):
        i += 0.2
        value += 0.2
        j = value
        temp = 0
        temp2 += 1

    if(temp2 == 5):
        temp2 = 0
    j += 1



'''
