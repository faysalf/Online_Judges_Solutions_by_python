def birthday_candles(candles):
    return candles.count(max(candles))

n = int(input())
candles = list(map(int,input().split()))
print(birthday_candles(candles))
