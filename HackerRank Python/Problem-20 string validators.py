s = input().strip()
result = 0
for i in range(len(s)):
    if s[i-1:i+1].isalnum():
        result += 1
if result>0:
    print("True")
else:
    print("False")
result = 0
for i in s:
    if i.isalpha():
        result += 1
if result>0:
    print("True")
else:
    print("False")
result = 0
for i in s:
    if i.isdigit():
        result += 1
if result>0:
    print("True")
else:
    print("False")
result = 0
for i in s:
    if i.islower():
        result += 1
if result>0:
    print("True")
else:
    print("False")
result = 0
for i in s:
    if i.isupper():
        result += 1
if result>0:
    print("True")
else:
    print("False")
