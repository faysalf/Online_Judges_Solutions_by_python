t = int(input())
for i in range(t):
    s= input()
    r= s[::-1]
    if s == r:
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")
