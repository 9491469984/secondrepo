class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def prepending(self,data):
        np=Node(data)
        np.next=self.head
        self.head=np
    def accending(self,data):
        na=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=na
    def insertion_at_specificposition(self,pos,data):
        
            ni=Node(data)
            if pos==0:
                ni.next=self.head
                self.head=ni
            else:
                ni=Node(data)
                temp=self.head
                for i in range(pos-1):
                    temp=temp.next
                ni.data=data
                ni.next=temp.next
                temp.next=ni
    def display(self):
        if self.head is None:
            print("head is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
    def delete_at_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        pre=self.head
        while temp.next:
            temp=temp.next
            pre=pre.next
        pre.next=None
    def delete_at_specificPosition(self,pos):
        temp=self.head.next
        pre=self.head
        for i in range(1,pos-1):
            temp=temp.next
            pre=pre.next
        pre.next=temp.next
        temp.next=None





l=Linkedlist()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4

l.prepending(5)

l.accending(60)

l.insertion_at_specificposition(1,25)
l.delete_at_begining()
l.delete_at_end()
l.delete_at_specificPosition(3)
l.display()