n = int(input())
row = n*4 -2
count = 1
column = n*2 -1
f = n
for i in range(1,row):
    for j in range(1,column):
        if i==column:
            print(chr(96+f))
        else:
            print("-",end="")
        count += 1
        if count==row:
            print()
            count = 0
    column -= 2

