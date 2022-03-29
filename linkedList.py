class Node:
    def __init__(self,data):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while(n!=None):
                print("<---",n.data,end="")
                n= n.ref
    def add(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

LL = LinkedList()
LL.print_ll()
LL.add(10)
LL.add(20)
LL.add(30)
LL.add(40)
LL.print_ll()
