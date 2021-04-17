#duitae right
'''
n = int(input())
li = []
lii = []
for i in range(n):
    a,b,c,d = input().split()
    li.append(a)
    lii.append([b,c,d])
m = input()
l = []
for i in range(n):
    if li[i] == m:
        l= (lii[i])
sm = 0
for i in l:
    sm += float(i)
print("%.2f"%(sm/3))
'''

n = int(input())
student_marks = {}
for i in range(n):
    name,*score = input().split()
    scores = list(map(float,score))
    student_marks[name] = scores
query_name = input()
print("%.2f"%(sum(student_marks[query_name])/3))
