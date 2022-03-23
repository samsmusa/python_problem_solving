from itertools import *
a = [1,2,3]
b = [4,5,6]
c= permutations("ABC")
d = combinations("ABC",2)
aa = map(''.join,c)
cc = map(''.join,d)
print(*cc)