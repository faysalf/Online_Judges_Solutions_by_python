import os
def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    unsorted = []

    for _ in xrange(n):
        unsorted_item = raw_input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
""" #duitae accepted
t = int(input())
unsorted = []
for _ in range(t):
    unsorted.append(input())

unsorted.sort(key=int)
for s in unsorted:
    print(s)
"""