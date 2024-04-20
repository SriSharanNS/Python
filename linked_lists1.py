from platform import node


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

a=Node("1")
b=Node("2")
c=Node("3")
d=Node("4")

a.next=b
b.next=c
c.next=d


def print_list(head):
    cur=head
    while cur is not None:
        print(cur.val)
        cur=cur.next

print_list(a)

def print_list1(head):
    if head==None:
        return
    else:
        print(head.val)
        print_list1(head.next)

print_list1(a)


