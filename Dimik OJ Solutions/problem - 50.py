                #duita e thik
T = int(input())
for _ in range(T):
    S = list(input().strip())
    for i in range (len(S)):
        S[i] = S[i-1] if S[i] == 'L' else S[i]
        S[i] = S[i+1] if S[i] == 'R' else S[i]
    print(''.join(S))









'''
T = int(input())
for _ in range(T):
    S = list(input())
    for index in range (len(S)):
        if S[index] == 'L':
            S[index] = S[index-1]
        elif S[index] == 'R':
            S[index] = S[index+1]
        else:
            S[index] = S[index]
    print(''.join(S))
'''
