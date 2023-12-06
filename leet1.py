b=[1,2,3,5,9,4];
a=b
t=9;
def show(a,t):
    c=[];
    i=0;
    j=len(a)-1;
    while(j>=i):
        
        if a[i]+a[j]==t:
            print(i,j,t);
            print(a[i],a[j])
            c.append(b.index(a[i]))
            c.append(b.index(a[j]));
            i=i+1
        elif a[i]+a[j]<t:
            print('*')
            i=i+1;
        elif a[i]+a[j]>t :
            j=j-1;
    return c;
print(show(a,t));
print(a[3],a[4])
