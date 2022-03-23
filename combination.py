# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

text, num = sys.stdin.readline().split(' ')
num = int(num)
text = sorted(text)

def cur(li,lent,arr,text):
    for i in li:
        text +=i
        if len(text)<lent:
            lis = li[li.index(i)+1:]
            cur(lis,lent,arr,text)
        else:
            if text not in arr:
                print(text)
                arr.append(text)
                text = text[:-1]
                continue
             
        text = text[:-1]
arry = []
for i in range(num):
    cur(text,i+1,arry,text='')
    
    
# alternative 
from itertools import *

s,k = input().split(' ')

for l in range(1,int(k)+1):
    for c in combinations (sorted(s),l):
        print(''.join(c))