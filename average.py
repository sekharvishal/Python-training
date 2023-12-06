class avg:
    def __init__(self):
        self.no=int(input("no of digits"))
        self.li=[]
        
        for i in range(self.no):
            self.li.append(int(input()))
    def avvg(self):
            self.sum=0
            for i in range(self.no):
                self.sum=self.sum+self.li[i]
            return (self.sum/self.no)
a=avg()
print(a.avvg())
