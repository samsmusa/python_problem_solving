# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
A = list(map(int, sys.stdin.readline().split (" ")))
B = list(map(int, sys.stdin.readline().split (" ")))

print(" ".join(list(str((i,j)) for i in A for j in B)))