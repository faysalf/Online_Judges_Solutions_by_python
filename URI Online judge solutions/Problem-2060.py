N = int(input())
li = list(map(int,input().split()))
two = 0
three = 0
four = 0
five = 0
for i in li:
    if i%2 == 0:
        two += 1
    if i%3 == 0:
        three += 1
    if i%4 == 0:
        four += 1
    if i%5 == 0:
        five += 1
print("%d Multiplo(s) de 2"%two)
print("%d Multiplo(s) de 3"%three)
print("%d Multiplo(s) de 4"%four)
print("%d Multiplo(s) de 5"%five)
