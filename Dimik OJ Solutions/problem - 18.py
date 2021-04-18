                            #duitae hoise
T = int(input())
for i in range(T):
    S = input()
    vowels,consonants = "AEIOUaeiou",'bcdfghjklmnpqrstvwxyzBCDFGHIJKLMNPQRSTVWXYZ'
    li1 = []
    li2 = []
    for j in S:
        if j in vowels:
            li1.append(j)
        elif j in consonants:
            li2.append(j)
    print("".join(li1),"".join(li2),sep = "\n")



    
'''
for T in range(int(input())) :
	s = input()
	vowel,consonant = 'aeiouAEIOU','bcdfghjklmnpqrstvwxyzBCDFGHIJKLMNPQRSTVWXYZ'
	f = ''
	ss = ''
	for i in s:
		if i in vowel:
			f += i
		elif i in consonant:
			ss += i
	print(f,ss,sep='\n')
'''
