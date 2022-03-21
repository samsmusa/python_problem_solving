
import sys
row, col = map(int, sys.stdin.readline().split (" "))
text = "WELCOME"

# top bar 
for j in range(row//2,0,-1):
    print((3*j)*"-"+".|."*(row//2+1-j)+".|."*(row//2-j)+(3*j)*"-")
    
# middle bar 
print((col-len(text))//2 * "-"+text+(col-len(text))//2 * "-")
    
# bottom bar 
for j in range(1,row//2+1):
    print((3*j)*"-"+".|."*(row//2+1-j)+".|."*(row//2-j)+(3*j)*"-")
    
    