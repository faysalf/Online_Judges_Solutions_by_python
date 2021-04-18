T = int(input())
for i in range(T):
    S = input()
    lis = []
    for character in S:
        number = ord(character)-64
        lis.append(number)
    for k in lis:
        print(k,end='')
    print()

'''
while True:
    S = input()
    lis = []
    a = (lis.append(ord(character)-64)for character in S)
    print(lis)
'''
