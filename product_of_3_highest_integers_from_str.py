str=input("Enter the string");

re=[]
r=[];


for i in range(0,(len(str))):
    if ((str[i]>='1')and(str[i]<='9')):
        re.append(str[i]);
print(re)
        
for i in range(0,len(re)-2):
    r.append(int(re[i])*int(re[i+1])*int(re[i+2]));
    print(r)
    
r.sort();
print(r[-1])
    
    
        
    
