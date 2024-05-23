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

    def chack_palindrome(self):
        arr=[]
        n=self.head
        while n is not None:
            arr.append(n.data)
            n=n.ref
        i,n=0,len(arr)-1
        while i<n:
            if arr[i]!=arr[n]:
                print('not a plaindrome')
                return
            n=n-1
            i=i+1
        print('string is plaindrome')





l=LinkedList()
s='malayalam'
for i in s:
    l.add_end(i)

l.print_ll()
print()
l.chack_palindrome()
