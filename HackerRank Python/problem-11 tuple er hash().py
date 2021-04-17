n = int(input())
int_list = list(map(int,input().split()))
new_tuple = tuple(int_list)
print(hash(new_tuple))

'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
'''
