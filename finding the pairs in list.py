l=[]
c=0;

n=int(input("please enter the size of the list"))

d=n-1;
for i in range (0,n):
    l.append(int(input()))

k=int(input("enter the value to be found"))

l.sort()


for i in range(0,n-2):
    while(c<d):
        z=l[i]+l[c]+l[d]
        if z<k:
            c=c+1
        elif z>k:
            d=d-1;
        elif z==k:
            
            
            print(l[i],l[c],l[d])
            c=c+1
            
    
