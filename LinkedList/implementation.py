class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.ref=self.head
            self.head=node
            

    def add_end(self,data):
        if self.head is None:
            print('ll is empty')
            return
        else:
            node=Node(data)
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=node

    def add_after(self,data,x):
        node=Node(data)
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print('element not present')
            return
        else:
            node.ref=n.ref
            n.ref=node

    def add_before(self,data,x):
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n is None:
            print('element not present')
            return
        else:
            node=Node(data)
            node.ref=n.ref
            n.ref=node

    def print_ll(self):
        n=self.head
        while n is not None:
            print(n.data,'--->',end="")
            n=n.ref


    def remove_begin(self):
        if self. head is None:
            print('empty')
            return
        else:
            self.head=self.head.ref

    def remove_end(self):
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None
    
    def remove_before(self,x):
        n=self.head
        while n.ref.ref is not None:
            if x==n.ref.ref.data:
                break
            n=n.ref
        if n is not None:
            n.ref=n.ref.ref
    
    def remove_after(self,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is not None:
            n.ref=n.ref.ref



        

        
# 10 20 30 40 50
            



l=LinkedList()
l.add_begin(10)
l.add_begin(20)
l.add_end(30)
l.add_before(25,30)
l.add_after(15,20)
l.print_ll()
print()


l.remove_before(30)
l.remove_after(15)
l.print_ll()

