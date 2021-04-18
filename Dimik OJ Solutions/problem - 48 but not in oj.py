#All are right...
T = int(input())
for i in range(T):
    N = int(input())
    li = list(map(int,input().split()))
    li2 = [j for j in range(li[0],li[-1])]
    if N-1 == len(li):
        print(*(set(li2)-set(li)))

        
'''
T = int(input())
for i in range(T):
    N = int(input())
    li = list(map(int,input().split()))
    li2 = [j for j in range(1,N+1)]
    if N-1 == len(li) and li[-1]<= N:
        print(*(set(li2) - set(li)))


'''
'''
def find_missing(lst): 
    return sorted(set(range(lst[0], lst[-1])) - set(lst))
lst = list(map(int,input().split()))
print(*find_missing(lst)) 
'''
