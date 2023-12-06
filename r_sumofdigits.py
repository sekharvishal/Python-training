def sum(a):
    if a==0:
        return a;
    else:
        return a+sum(a-1);
a=int(input("value"));
print(sum(a));
