import sys

text, num = sys.stdin.readline().split(' ')
num = int(num)
text = sorted(text)

def cur(li,lent,text):
    for i in li:
        text +=i
        if len(text)!=lent:
            lis = li.copy()
            lis.remove(i)
            cur(lis,lent,text=text)
        else:
            print(text)
            text = text[:-1]
            continue
             
        text = text[:-1]
        
cur(text,num,text='')