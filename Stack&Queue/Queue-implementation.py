class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None

    def enqueue(self,data):
        node=Node(data)

        if self.rear is None:
            self.rear=node
            self.front=node
        else:
            self.rear.ref=node
            self.rear=node

    def dequeue(self):
        popped=self.front
        if popped is not None:
            self.front=self.front.ref
            if self.front is None:
                self.rear=None
            print('\n',popped.data,'removed')

    def print_queue(self):
        n=self.front
        while n is not None:
            print(n.data,'--->',end="")
            n=n.ref


    def peek(self):
        print(f" \n{self.front.data} is top element")


q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)


q.print_queue()

q.peek()

q.dequeue()
q.print_queue()