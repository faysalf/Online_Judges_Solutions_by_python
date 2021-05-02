def super_digits(n,k):
    li = map(int,list(n))
    return find_super_digits(str(sum(li)) * int(k))

def find_super_digits(p):
    if len(p)==1:
        return int(p)
    else:
        l = map(int, list(p))
        return find_super_digits(str(sum(l)))

if __name__=="__main__":
    n,k = input().split()
    print(super_digits(n,k))





'''#Runtime Error ase
def super_digit(n):
    l = list(map(int,list(n)))
    if sum(l)<10:
        return sum(l)

    return super_digit(str(sum(l)))

if __name__=="__main__":
    n,k = input().split()
    print(super_digit(n*int(k)))'''