S = input()
step = int(input())
for i in S:
    if i == ' ':
        print(" ",end="")
        continue
    unicode = ord(i)
    c_unicode = 0
    if unicode <= 90:
        r = (unicode - 65 - step)%26
        c_unicode = r + 65
    elif (unicode <= 122) and (unicode >= 97):
        r = (unicode - 97 - step) % 26
        c_unicode = r + 97
    print(chr(c_unicode),end='')

