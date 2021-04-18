m,n = map(int,input().split())
li = []
lii = []
f = []
for _ in range(m):
    word, salary = input().split()
    li.append(word)
    lii.append(int(salary))
for _ in range(n):
    s = ""
    total_salary = 0
    while True:
        ss = input()
        if ss==".":
            break
        s += ss
    for i in li:
        total_salary += s.count(i) * lii[li.index(i)]
    print(total_salary)

'''
m,n = map(int,input().split())
li = []
lii = []
for _ in range(m):
    word, salary = input().split()
    li.append(word)
    lii.append(int(salary))
s = []*n
total_salary = []
for _ in range(n):
    while True:
        ss = input()
        if ss==".":
            break
        s.append(ss)
for j in range(n):
    indx = s[j]
    one = 0
    for i in li:
        one += (indx.count(i) * lii[li.index(i)])
    total_salary.append(one)
print(total_salary)
'''
