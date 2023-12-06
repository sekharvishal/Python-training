num=int(input('enter the num'));


def sum(num):
    if num==0:
        return 0;
    elif num==1:
        return 1;
    else:
        return num+sum(num-1);
res=sum(num);
print(res);




        
