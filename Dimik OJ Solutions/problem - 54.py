T = int(input())
for _ in range(T):
    sm1 = 1
    sm2 = 1
    s1,s2 = map(str,input().split())
    for i in s1:
        sm1 *= ord(i)
    for j in s2:
        sm2 *= ord(j)
    if sm1%97 == sm2%97:
        print("YES")
    else:
        print("NO")

        
#hash key: hash(vowels)
