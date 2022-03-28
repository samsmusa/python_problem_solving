size = 4
alp = 'abcdefghijklmnopqrstuvwxyz'
# top bar 
for i in range(1,size+1):
    # te = 
    print(int("".join([str(j) for j in range(1,i+1)] + [str(j) for j in range(i-1,0,-1)])))