def rev(a):
    s=len(a);
    
    if s==0:
        return a;
    else :
   
   
        return a[s-1]+rev(a[0:s-1]);
a=input('enter the string ')


print(rev(a));
