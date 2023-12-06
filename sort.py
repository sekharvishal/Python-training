a=list(map(int,input().split(',')));
print(a)

def sort(a):
    if len(a)>1:
        m=len(a)//2;
       

        l=a[:m];
        r=a[m:];

        sort(l);
        sort(r);
        i=j=k=0;
        while i<len(l) and j<len(r) :
            if l[i]<r[j]:
                a[k]=l[i];
                k+=1;
                i+=1;
            else:
                a[k]=r[j];
                k+=1;
                j+=1;
        while i<len(l):
            a[k]=l[i]
            i+=1;
            k+=1;
        while j<len(r):
            a[k]=r[j];
            j+=1;
            k+=1;
sort(a)
print(a)
