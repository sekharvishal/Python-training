a=[1,4,6,8,10]
res=[];

re=0;
for i in range(len(a)):
    re=0
    for j in range (len(a)):
       
        re=re+(abs(a[j]-a[i]));
    res.append(re)
    
print(res)
  
   
   
       
   
   
        
    
 

        
        
