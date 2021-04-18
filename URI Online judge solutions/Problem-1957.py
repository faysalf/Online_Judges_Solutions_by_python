while True:
    N = int(input())
    res = hex(N).lstrip("0x").upper()
    print(res)
