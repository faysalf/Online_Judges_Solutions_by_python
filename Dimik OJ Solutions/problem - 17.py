T = int(input())
for i in range(T):
    string = input().lower()
    count = 0
    vowel = ['a','e','i','o','u']
    for r in string:
        if r in vowel:
            count += 1
    print("Number of vowels =",count)
