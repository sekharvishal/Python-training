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
    

        
        
    
