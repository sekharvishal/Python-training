a=[2,3,4,5,6]
c=0;
for i in range(len(a)+1):
    print(a[i],"*")
    c=0;
    for j in range(1,a[i]):
        print(a[i])
        if(a[i]%j==0):
            c=c+1;
    if(c==2):
        print(a[i]);
    else:
        print('n0');
    
