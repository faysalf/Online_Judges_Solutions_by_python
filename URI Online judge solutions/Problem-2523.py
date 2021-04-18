while True:
    try:
        result = ""
        S = input()
        N = int(input())
        li = [int(i) for i in input().split()]
        for j in li:
            result += S[j-1]
        print(result)
    except EOFError:
        break
