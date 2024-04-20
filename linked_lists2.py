class linked_1:
    def __init__(self,val,nextnode=None):
        self.val=val
        self.nextnode=nextnode


n1=linked_1("a")
n2=linked_1("b")
n3=linked_1("c")
n4=linked_1("d")

n1.nextnode=n2
n2.nextnode=n3
n3.nextnode=n4

curr=n1
while True:
    print (curr.val)
    if curr==None:
        break
    curr=curr.nextnode 
