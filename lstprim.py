
a=int(input("Enter the no of elements "));
l=[];
for i in range(a):
    l.append(int(input()))
s=0;


prime=[]
for i in l:
    c=0;
    for j in range (1,i):
        if i%j==0:
            c=c+1;
    if c==1:
        prime.append(i);
    
print(prime);
prime.sort();
print(prime);
for i in range(len(prime)-1):
   
    s=s+l[i];
print(s);
