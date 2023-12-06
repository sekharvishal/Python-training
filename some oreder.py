a="aaabbc";
c=0
for i in range (len(a)+2):
    c=0
    while(c<len(a)-1):
        c=0
        for j in range(c,len(a)):
            c=0
            if a[c]==a[j]:
                c=c+1
    print(c,a[i])
            
