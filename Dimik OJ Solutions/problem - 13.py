'''
import math
T = int(input())
for i in range(T):                        #for T in range(in(input())):
    string = list(map(str,input().split()))
    l = len(string)
    d = {}
    for j in string:
        d[j] = string.count(j)
    count = 1
    for k in d.keys():
        if d[k] > 1:
        
#d[k],str a word kotobar ase ta call korbe, jodi ak e word barbar thake
#tahole ta 1 theke boro hobe. ar ta 1barer beshi asle tar factorial ber korbo.

            count *= math.factorial(d[k])
    if count == 0:                      #count jodi 0 hoye jay tahole count ke 1
        count = 1                       #kore dite hobe tai duti count use hoise
    print("1/%d"%(math.factorial(l)//count))

#l ke factorial kora hobe. ar take count dara vag kora hobe. karon nPr a r ar man
#hobe kono word repeat hole. ar kono word repeat hole ta count a joma hoy. tai count
#a joma hoy. ar count a kono word repeat na hole tar man 0 hobe ja fact0 = 1 dara vag hobe
#****details khatay
'''

import math
for T in range(int(input())):
    string = list(map(str,input().split()))
    l = len(string)
    d = {}
    for i in string:
        d[i] = string.count(i)
    count = 1
    for j in d.keys():
        if d[j] > 1:
            count = math.factorial(d[j])
    if count == 0:
        count = 1
    print("1/%d"%(math.factorial(l)//count))
