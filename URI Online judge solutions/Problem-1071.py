X = int(input())
Y = int(input())
s = 0
for i in range(Y+1,X):
    if i%2==1:
        s += i
print(s)
