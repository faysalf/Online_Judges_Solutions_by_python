import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    return "\n".join(word_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

'''
import textwrap
s = input()
w = int(input())
wrapper = textwrap.TextWrapper(width=w) 
word_list = wrapper.wrap(text=s)
for i in word_list:
    print(i)
'''

'''
s = input()
w = int(input())
ln = 0
st = ""
for i in range(len(s)):
    st += s[i]
    ln += 1
    if ln == w:
        print(st)
        ln = 0
        st = ""
if ln>0:
    print(st)
'''
