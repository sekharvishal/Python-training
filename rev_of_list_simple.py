a=[1,2,3,4,5,6,7,8];
b=15;

for i in range(0,int(len(a)/2)):
    a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i];
print(a)
