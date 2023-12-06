# reversing a string using recursion
a='abc'
def rev(a):
    if (len(a)==1):
        return a[len(a)-1];
    else:
        return (a[len(a)-1]+rev(a[:len(a)-1]));
x=a
print(x)


a=[100,16,1,5,2,8,5,9];
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)


a=list(map(int,input().split(' '))); # adding the elements in the list 

print(a); # print the list
print(a[::-1]);  # printing the reverse of list normal mtd
def rev(a):
     if (len(a)==1):
         return a[len(a)-1]
     else:
        return (a[len(a)-1]+rev(a[:len(a)-1]));
a=['a','b','c','s','f','1','4']
print(rev(a));
    

        
        
    
def revn(a,r):
    if a<=9:
        return r*10+a;
    else:
 
        return revn(a//10,r*10+a%10)
a=int(input("Enter the values"))
r=0;
print(revn(a,r))


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

