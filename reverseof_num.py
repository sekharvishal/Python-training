def revn(a):
    if a<=9:
        return a;
    else:
        print(a)
        
        return (a%10)+revn(a//10)
a=1234;
print(revn(a))
