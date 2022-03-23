# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
S = list(map(int,input().split(' ')))
N = int(input())
size = []
price = []
for i in range(N):
    k = list(map(float,input().split(' ')))
    size.append(k[0])
    price.append(k[1])
s = list(Counter(S).keys())
q = list(Counter(S).values())
income = 0
for i in range(N):
    if size[i] in s:
        
        if q[s.index(size[i])] > 0:
            q[s.index(size[i])] = q[s.index(size[i])]-1
            income += price[i] 
print(int(income))