# reversing a string using recursion
a='abc'
def rev(a):
    if (len(a)==1):
        return a[len(a)-1];
    else:
        return a[len(a)-1]+rev(a[:len(a)-1]);
    
x=rev(a)
print(x)


