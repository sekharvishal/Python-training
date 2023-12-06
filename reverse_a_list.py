lst=[1,2.0,'vishal',5,12.4]
print(lst,len(lst));
n=len(lst);
n=n-1;

for i in range(0,n//2):
    lst[i],lst[n-i]=lst[n-i],lst[i];
print(lst)
