a=[1,2,3,4,5,10,9,7];
a=sorted(a);
k=10

i=0;
j=len(a)-1;

while j>=i:
    
    if a[i]+a[j]==k:
        print(a[i],a[j]);
        i=i+1;
    elif a[i]+a[j]<k :
        i=i+1;
    elif a[i]+a[j]>k :
        j=j-1;

        
print('another apporach')



for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]+a[j]==k :
            print(a[i],a[j]);
