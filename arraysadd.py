a=[1,2,3,6,4,8,5,3,6,8,0,12,45]
b=[6,4,9,37,9,5,7,8,0]
a.sort();
b.sort();
c=[]
print(len(a)+len(b))
if len(a)>len(b):
 for i in range((len(a))):
    if (i<len(a))and (i<len(b)):
  
        if a[i]< b[i]:
            c.append(a[i])
            c.append(b[i])
        else:
            c.append(b[i])
            c.append(a[i])
    else:
        if len(a)>len(b):
            c.append(a[i])
        else:
            c.append(b[i])
else:
 for i in range((len(b))):
    if (i<len(a))and (i<len(b)):
  
        if a[i]< b[i]:
            c.append(a[i])
            c.append(b[i])
        else:
            c.append(b[i])
            c.append(a[i])
    else:
        if len(a)>len(b):
            c.append(a[i])
        else:
            c.append(b[i])
        
        
print(c)
print(len(c))

