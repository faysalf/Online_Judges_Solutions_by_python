#duita aktu differant vabe kora
n = int(input())
nt,reg = 0.0, 0
for _ in range(n):
    m,note = input().split()
    if float(note)> nt:
        nt = float(note)
        reg = int(m)
if nt>=8:
    print(reg)
else:
    print("Minimum note not reached")

'''
n = int(input())
nt,reg = 0.0, 0
for _ in range(n):
    m,note = map(float,input().split())
    if note> nt:
        nt = note
        reg = m
if nt>=8:
    print(int(reg))
else:
    print("Minimum note not reached")
'''
