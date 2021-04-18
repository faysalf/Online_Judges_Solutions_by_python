S = input()
r = S.count("1")
if r%2==0:
    S += "0"
else:
    S += "1"
print(S)
