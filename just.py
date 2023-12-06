print("welcome bcak")
a=[1,53,6,7,3,23,68,21];
n=len(a)-1;
for i in range(n//2+1):
    a[i],a[n-i]=a[n-i],a[i]
    print(i,a[i])
print(a)
