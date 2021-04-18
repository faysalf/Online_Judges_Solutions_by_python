while True:
    try:
        L = int(input())
        Vi = list(map(int,input().split()))
        mx = max(Vi)
        if mx<10:
            print("1")
        elif mx>=10 and mx<20:
              print("2")
        else:
            print("3")
    except:
        break
