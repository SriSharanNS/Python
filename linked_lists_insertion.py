class Node:

    def __init__(self,data):

        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):

        self.head=None

    def push(self,newdata):

        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode

    def append(self,newdata):

        newnode=Node(newdata)

        if self.head is None:
            newnode=self.head
            return
        
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode

    def pos(self,prevnode,newdata):

        if self.head is None:
            print("list is empty")
            return

        newnode=Node(newdata)

        newnode.next=prevnode.next
        prevnode.next=newnode

    def del_front(self):

            if self.head is None:
                print("no data")
                return

            temp=self.head
            self.head=self.head.next
            del(temp)

    def del_end(self):

            if self.head is None:
                print("no data")
                return

            cur=self.head
            prev=None
            while(cur.next):
                prev=cur
                cur=cur.next
                
            prev.next=None
            del(cur)        


            

    def printList(self):

        temp = self.head

        while (temp):
            print(temp.data)
            temp = temp.next       


llist=Linkedlist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.append(7)
llist.append(6)
llist.del_front()
llist.push(8)
llist.pos(llist.head,5)
llist.del_end()
llist.del_end()
llist.printList()
