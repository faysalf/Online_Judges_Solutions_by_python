while True:
    n = float(input())
    re = ((1.61803398874989)**n) - ((-0.61803398874989)**n)
    print("%.1f"%(re/5**0.5))
