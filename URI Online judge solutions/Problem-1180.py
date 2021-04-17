    #duitae accepted

N = int(input())
X = list(map(int,input().split()))
m_in = min(X)
ind = X.index(m_in)
print("Menor valor: %d"%m_in)
print("Posicao: %d"%ind)

'''
N = int(input())
X = list(map(int,input().split()))
m_in = min(X)
position = 0
for i in range(len(X)):
    if X[i] == m_in:
        position = i
print("Menor valor: %d"%m_in)
print("Posicao: %d"%position)
'''
