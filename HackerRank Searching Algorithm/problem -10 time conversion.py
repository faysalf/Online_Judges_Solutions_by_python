s = input()
am_or_pm = (s[-2:])
s = s[:-2]

fs = list(map(str,s.split(":")))

hour = fs[0]

if am_or_pm == "AM":
    if fs[0] == "12":
        fs[0] = "00"

else:
    if int(fs[0])<12:
        fs[0] = str(12+int(fs[0]))

print(":".join(fs))
