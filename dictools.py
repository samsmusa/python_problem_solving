# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)
a,b = map(int,input().split(' '))
A = [input() for i in range(a)]
B = [input() for i in range(b)]
for j,i in enumerate(A):
    d[i].append(j+1)
for i in B:
    if d[i] != []:
        dd = list(map(str,d[i]) )
        print(' '.join(dd))
    else:
        print(-1)