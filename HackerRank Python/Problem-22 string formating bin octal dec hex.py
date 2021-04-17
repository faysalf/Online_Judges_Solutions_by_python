def print_formatted(n):
    ln = len(bin(n)[2:])
    for i in range(1,n+1):
        print(str(i).rjust(ln," "),end=" ")
        '''
rjust() method diye right site theke sajano hoy and space remove kore fillup kora hoy
rjust(ln," ") ln width replace by " ". '''
        print(str(oct(i)[2:]).rjust(ln," "),end=" ")
        print(str((hex(i)[2:]).upper()).rjust(ln," "),end=" ")
        print(str(bin(i)[2:]).rjust(ln," "),end=" ")
        print()
if __name__ == "__main__":
    n = int(input())
    print_formatted(n)

'''
#rjust() method diye right site theke element sajano thake & gap fillup kore
l = 5
for i in range(1,l+1):
    print(i.rjust(l," "),end=" ")
'''

'''
n = int(input())
for i in range(1,n+1):
    print(i,oct(i)[2:],(hex(i)[2:]).upper(),bin(i)[2:]) #just bin er original bit
'''
