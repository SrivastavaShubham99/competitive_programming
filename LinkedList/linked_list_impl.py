

class Node : 
    def __init__(self,data) :
        self.data=data
        self.next=None


class LinkedList : 
    def __init__(self) :
        self.head=None
        self.size=0

    #creating new node 
    # make sure to insert at the last therefore we iterate till the last node
    # in order to get the reference of the last node ......
    def insert_at_back(self,data) : 
        node=Node(data)
        self.size+=1
        if self.head==None : 
            self.head=node
        else : 
            last=self.head
            # here is the crux of the method make sure to be stand at last
            # insert the element at the last
            while last.next!=None : 
                last=last.next
            last.next=node

    def insert_at_front(self,data) : 
        node=Node(data=data)
        self.size+=1
        if self.head==None : 
            self.head=node
        else : 
            node.next=self.head
            self.head=node

    def insert_at_pos(self,data,pos) : 
        node=Node(data=data)
        self.size+=1
        temp_pos=0
        temp_pointer=self.head
        if self.head==None : 
            self.head=node
        if pos==self.size :
            self.insert_at_back(data=data)
        if self.size==0 : 
            self.insert_at_front(data=data)
        if pos > self.size or pos < 0 : 
            print("abe kuch bhi krwabe kya")
            return 
        while temp_pos < pos-1 : 
            temp_pointer=temp_pointer.next
            temp_pos+=1
        aux_store=temp_pointer.next
        temp_pointer.next=node
        node.next=aux_store

    def printList(self) : 
        temp=self.head
        while temp.next!=None : 
            print("data -> {}, ".format(temp.data))
            temp=temp.next
            if temp.next==None : 
                print("data -> {}".format(temp.data))

    def delete_at_front(self) : 
        self.head=self.head.next
        self.size-=1

    """logic here is to use the slow and the fast pointer,
     move both the pointers simuntaneously untill
     the fast pointer reached to the last node and slow pointer just
     behind that will be standing at the last node,then make it NULL
     will do the job for us ..... """

    def delete_at_back(self) : 
        if self.size==0 : 
            print("list is empty!")
        else : 
             current_node=self.head
             prev_node=self.head
             while current_node.next!=None :
                prev_node=current_node
                current_node=current_node.next
             prev_node.next=None
             self.size-=1



    def delete_at_pos(self,pos) : 
        pass

    def delete_by_value(self,value) : 
        pass



if __name__ =='__main__' : 
    linkedList=LinkedList()
    linkedList.insert_at_back(1)
    linkedList.insert_at_back(2)
    linkedList.insert_at_back(3)
    linkedList.insert_at_back(4)
    linkedList.delete_at_front()
    linkedList.insert_at_pos(9,2)
    linkedList.insert_at_front(5)
    linkedList.insert_at_front(6)
    linkedList.delete_at_back()
    linkedList.printList()


