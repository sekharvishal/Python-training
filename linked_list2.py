class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
class LL:
    def __init__(self):
        self.head=None;
    def IAB(self,data):
        n1=Node(data);
        if self.head is None:
            self.head=n1
            return
        else:
            n1.next=self.head
            self.head=n1
    def PrintLL(self):
        c=self.head
        while(c):
            print(c.data,end=" ")
            c=c.next
l1=LL();
l1.IAB('a')
l1.PrintLL()
l1.IAB('n')
l1.IAB("c")
l1.PrintLL()
