while True:
    try:
        one = 0
        N = int(input())
        li = input().split()
        one += li.count("1")
        if one >= ((N*2)/3):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break

