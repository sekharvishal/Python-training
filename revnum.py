l=[1,2,3,4,5,6,7,8,9]
l=list(map(str,l));
def rev(l):
    if len(l)==1:
        return l[len(l)-1];
    else:
        return l[len(l)-1]+rev(l[:len(l)-1])

print(rev(l))
