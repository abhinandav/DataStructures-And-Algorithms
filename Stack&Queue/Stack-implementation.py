class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        node=Node(data)
        if self.top is None:
            self.top=node
        else:
            node.ref=self.top
            self.top=node

    def pop(self):
        popped=self.top
        if popped is not None:
            self.top=self.top.ref
            print('\n',popped.data,'removed')

    def print_stack(self):
        n=self.top
        while n is not None:
            print(n.data,'--->',end="")
            n=n.ref
    def peek(self):
        print(f" \n{self.top.data} is top element")


s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.print_stack()

s.pop()
s.print_stack()