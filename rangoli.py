size = 3
alp = 'abcdefghijklmnopqrstuvwxyz'
# top bar 
for i in range(size-1,0,-1):
    te = [alp[j] for j in range(size-1,i-1,-1)] + [alp[j] for j in range(i+1,size)]
    print('-'*(i*2)+"-".join(te)+'-'*(i*2))
# middle bar 
te = [alp[j] for j in range(size-1,0,-1)] + [alp[j] for j in range(0,size)]
print("-".join(te))
# bottom bar 
for i in range(1,size):
    te = [alp[j] for j in range(size-1,i-1,-1)] + [alp[j] for j in range(i+1,size)]
    print('-'*(i*2)+"-".join(te)+'-'*(i*2))