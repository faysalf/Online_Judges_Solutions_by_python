'''s = input()
print(" ".join(w[:1].upper()+w[1:] for w in s.split(" ")))
'''
#hoise
def solve(s):
    return " ".join(w[:1].upper()+w[1:] for w in s.split(" ")))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

