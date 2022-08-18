# https://www.geeksforgeeks.org/linked-list-set-1-introduction/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def printData(self):
        temp = self.head
        while(temp):
            print(str(temp.data)+"--->",end="")
            temp = temp.next
        print("")

    def pushToFront(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pushToBack(self,data):
        new_node = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

            

ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second
second.next = third
ll.printData()

ll.pushToFront(10)

ll.printData()

ll.pushToBack(11)

ll.printData()