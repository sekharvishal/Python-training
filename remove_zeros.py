a=[1,2,0,5,0,6,0];
idr=0;
for i in range(len(a)):
    if a[i]==0:
        a.remove(a[i])
        a.append('0');


print(a);
