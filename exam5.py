# a python code to interchange the first and last elements in the list
class lst:
    def __init__(self,lt):
        self.lt=lt;
    def chage(self):
        self.lt[0],self.lt[-1]=self.lt[-1],self.lt[0]
        return self.lt
lt=[1,7,3,4,6,7]
ls=lst(lt);
print(ls.chage())
