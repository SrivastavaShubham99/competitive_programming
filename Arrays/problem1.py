

#creating node con containing value and pointer to the next node.
#Linked List contains the series of these nodes attached with each
#other and are accessed with the help of pointers reference.
class Node() : 
    def __init__(self,value,next):
        self.value=value
        self.next=next


def main() : 
    #creating nodes
    head=None
    for i in range(1,6): 
        head=Node(i,head)
    
    #traversing the created nodes from above using the 
    #next reference value present in each node...

    while head!=None : 
        print('{}'.format(head.value))
        head=head.next

    #searching particular element in the Linked List .
    #traversals in the Linked Lists are linear in time we have 
    #start from the first node and ends until last 

    n1=Node("shubham",None)
    n2=Node("kakarot",n1)
    n3=Node("vegeta",n2)
    n4=Node("gohan",n3)

    head=n4

    while head.next!=None : 
        print('{}'.format(head.value))
        head=head.next

if __name__=="__main__" : 
    main()

