
from pdb import line_prefix


class Node():
    def __init__(self,value):
        self.value=value
        self.next=None


#interating version of the linked list..

class LinkedList() : 

    def __init__(self):
        self.head=None


    def insert_at_front(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node


    def insert_at_last(self,value):
        new_node=Node(value)
        if self.head==None : 
            self.head=new_node
        temp_node=self.head
        while temp_node.next is not None : 
            temp_node=temp_node.next
        temp_node.next=new_node
        

    def insert_after_node(self,value,data): 
        new_node=Node(value)
        node=self.head
        while node.value==data:
            node=node.next
        new_node.next=node.next
        node.next=new_node


    def insert_before_node(self,value,data):
        pass


    def traverseList(self):
        if self.head==None:
            print("linked list is empty")
        else : 
            node=self.head
            while node is not None : 
                print("value ===>>>>> {}".format(node.value))
                node=node.next
        

    def delete_at_front(self):
        front_node=self.head
        prev_node=front_node.next
        self.head=prev_node
        front_node.next=None
        

    def delete_at_last(self) : 
        if self.head==None :
            print("list is empty!")
        else :
            node=self.head
            while node.next.next != None :
                node=node.next
            node.next=None


    def length(self) : 
        node=self.head
        count=1
        while node.next!=None : 
            count+=1
            node=node.next
        return count


    def find_mid(self) : 
        temp_node=self.head
        for i in range(self.length()/2) : 
            temp_node=temp_node.next
            i+=1
        return temp_node.value
        

    



linkedList=LinkedList()
linkedList.insert_at_front(1)
linkedList.insert_at_front(2)
linkedList.insert_at_front(3)
linkedList.insert_at_front(4)
linkedList.insert_at_front(5)

print("element at middle -> {}".format(linkedList.delete_mid()))
linkedList.traverseList()