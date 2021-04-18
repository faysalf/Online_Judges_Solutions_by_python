top, time, ans, fishing_time, bait = [0]*5
while 1:
    try:
        d = input().strip()
    except EOFError:
        break
    if d == "lunch":
        time += 10
        continue
    if d == "fish":
        if top < 1 or (ans and (fishing_time < 20 or time < 60)):
            fishing_time += 10;time += 10
            continue
        ans += 1; fishing_time = 0; time = 0; top -= 1; continue 
    if d == "bait":
        time += 10
        if top == 3:
            continue
        bait += 1
        if bait == 2:
            top += 1;bait = 0;continue
print(ans)
