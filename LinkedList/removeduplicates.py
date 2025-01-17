class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None
  

    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node

        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=node

    def print_ll(self):
        n=self.head
        while n is not None:
            print(n.data,'--->',end="")
            n=n.ref

    def remove_duplicates(self):
        seen=set()
        prev=None
        n=self.head
        while n is not None:
            if n.data  not in seen:
                seen.add(n.data)
                prev=n
            else:
                prev.ref=n.ref
            n=n.ref
        







l=LinkedList()
a=[10,20,90,10,40,30,40,50]
for i in a:
    l.add_end(i)

l.print_ll()
print()

l.remove_duplicates()
l.print_ll()