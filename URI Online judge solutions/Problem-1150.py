X = int(input())
Z = 0
sum = X
count = 1
while Z <= X:
    Z = int(input())
while sum<=Z:
    sum += (X + count)
    count += 1
print(count)
