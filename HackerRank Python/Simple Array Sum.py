import os

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return (sum(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') #environ os er akti object, output
                                                #path tar akti variable. 'w' write korar jonno

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')  #resulttike write kore str kore new line print

    fptr.close()                    #os.environ close
