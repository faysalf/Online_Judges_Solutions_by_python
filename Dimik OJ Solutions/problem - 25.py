T = int(input())
for i in range(T):
    def compute_lcm(x, y):
       if x > y:
           greater = x
       else:
           greater = y
       while(True):
           if((greater % x == 0) and (greater % y == 0)):
               lcm = greater
               break
           greater += 1
       return lcm
    a,b = map(int,input().split())
    print("LCM =",compute_lcm(a,b))


'''holona keno?
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    if a>b:
        greater = a
    else:
        greater = b
    while a>b or b>a:
        if greater%a==0 and greater%b==0:
            print("LCM =",greater)
            break
        greater += 1
'''
