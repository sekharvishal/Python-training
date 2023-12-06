l=[1,2,3,4,5,6,7];
l=sorted(l);

k=7

i=0;
j=len(l)-1;
m=0;
while(i<=j):

    
    m=(i+j)//2
    if l[m]<k :
    
        i=m+1;
    elif l[m]>k :
       
        j=m-1;
        
    elif l[m]==k :
        print(m);
        break ;

def binsrch(l):
    i=0;
    j=len(l)-1;
    m=0;
    while(i<=j):
    
        m=(i+j)//2
        if l[m]<k :
    
            i=m+1;
        elif l[m]>k :
       
            j=m-1;
        
        elif l[m]==k :
            return m;
    return -1;
x=binsrch(l)
if (x==-1):
    print('not found');
else:
    print(x)
    
