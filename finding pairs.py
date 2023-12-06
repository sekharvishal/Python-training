l=[1,2,3,4,7,10,6,8,12,19,5,0];
l.sort()
print(l);
k=12;
a=0;
b=(len(l)-1);
print(l[a],l[b],a,b)

while(a<b):
  if a<(len(l)-1):
    c=l[a]+l[b]
    if c==k:
        print(l[a],l[b])
        a=a+1
        
    elif c<k:
        a=a+1
    else:
        b=b-1;

