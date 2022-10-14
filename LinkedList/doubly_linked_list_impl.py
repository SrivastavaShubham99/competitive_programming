
class Node :
    def __init__(self,data) :
        self.data=data
        self.next=None
        self.prev=None

"""
   1. Doubly linked list can be iterate or access from both the directions.
   2. Using the head we can access the data from the front.
   3. While access data from the front update head with next pointer.
   4. Using the tail we can access the data from the back.
   5. While access data from the back update tail with prev pointer.
   """
class DoubleLinkedList():
    def __init__(self) : 
        self.head=None
        self.tail=None
        self.size=0

    def insert_at_front(self,data) :
        new_node=Node(data=data)
        self.size+=1
        if self.head==None :
            self.head=self.tail=new_node
        else :
            new_node.prev=None
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insert_at_back(self,data) :
        self.size+=1
        new_node=Node(data=data)
        if self.head==None : 
            self.tail=self.head=new_node
        else :
            self.tail.next=new_node
            new_node.prev=self.tail
            new_node.next=None
            self.tail=new_node

    def insert_at_middle(self) :
        pass

    def insert_at_pos(self,pos) : 
        pass
            

    """head stands at the front of the double linked list...
       Note : 
       1. iterate from the front using head and update the head using the next
          pointer in order to get the data from the front.
       2. iterate from the back using tail and update the tail using the prev
          pointer in order to get data from the backside of the doubly linked
          list."""

    def print_from_front(self) :
        while self.head!=None :
            print("data -> {}".format(self.head.data))
            self.head=self.head.next
    
    """ tail always stands at the last node because we create it only at the creation
        of the first node and after that we doesn't update tail.Therefore it always 
        stands at the last node ...prev pointer knows the chain from the back and head
        knows the chain from the front ........"""

    def print_from_back(self) :
        while self.tail!=None :
            print("data -> {}".format(self.tail.data))
            self.tail=self.tail.prev


""" driver function executing and creating instances here only """
if __name__=="__main__" :
    dlinked_list=DoubleLinkedList()
    dlinked_list.insert_at_front("1")
    dlinked_list.insert_at_front("2")
    dlinked_list.insert_at_front("3")
    dlinked_list.insert_at_front("4")
    dlinked_list.insert_at_back("5")
    dlinked_list.insert_at_back("6")
    dlinked_list.print_from_front()



