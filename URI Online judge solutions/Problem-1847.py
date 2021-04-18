A,B,C = map(int,input().split())
if (A>B):
    if (B<C):
        print(":)")
    else:
        if (A-B > B-C):
            print(":)")
        else:
            print(":(")
elif (A<B):
    if (B>C):
        print(":(")
    else:
        if (B-A > C-B):
            print(":(")
        else:
            print(":)")
else:
    if (B<C):
        print(":)")
    else:
        print(":(")
