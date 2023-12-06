def mrgesort(ary):
    if len(ary)>1:

        mid=len(ary)//2;
        l=ary[:mid];
        r=ary[mid:];
       
      
        mrgesort(l)
        mrgesort(r)
        i=j=k=0;
        while i<len(l) and j<len(r) :
            if l[i]<=r[j]:
                ary[k]=l[i];
                i=i+1;
            else:
                ary[k]=r[j] 
                j=j+1;
            k=k+1;
        while i<len(l):
            ary[k]=l[i];
            j=j+1;
            k=k+1;

ary=[12,5,2,67,35,13]


mrgesort(ary)
print(ary)


            
