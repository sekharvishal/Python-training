def revn(a,r):
    if a<=9:
        return r*10+a;
    else:
 
        return revn(a//10,r*10+a%10)
a=int(input("Enter the values"))
r=0;
print(revn(a,r))
