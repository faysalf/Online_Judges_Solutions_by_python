                #duitae right
T = int(input())
for _ in range(T):
    s,sub = map(str,input().split())
    sub_len = len(sb)
    r = 0
    for i in range(len(s)):
        if s[i:i+sub_len] == sub: #i theke i+sub_len porjonto dekhbe and sub er sathe milabe
            r += 1
    print(r)


'''
t = int(input())
for i in range(t):
    main, sub = map(str, input().split())
    count = 0
    while main.find(sub)!=-1:
        count = count + 1
        y = main.find(sub)
        main = main[y+1:]
    print(count)
    '''
