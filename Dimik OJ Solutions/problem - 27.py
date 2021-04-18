T = int(input())
for i in range(T):
    ch = input()
    if ch.isupper() == True:
        print("Uppercase Character")
    elif ch.islower() == True:
        print("Lowercase Character")
    elif ch.isdigit() == True:
        print("Numerical Digit")
    else:
        print("Special Character")
