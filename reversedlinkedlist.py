class Node:
    def __init__(self,data):
        self.head=None
        self.data=data

class linked_list:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def detectLoop(self):
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True

        return False

    def delete(self,deleted):
        temp=self.head
        if temp.data == deleted:
            self.head=temp.next
        while temp != None :
            if temp.data==deleted:
                break
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp=None


llist = linked_list()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.printlist()
llist.reverse()
llist.printlist()
print(llist.detectLoop())
