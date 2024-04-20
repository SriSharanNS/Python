def search(list,item):
    l=0
    u=len(lis1)-1

    while l<=u:
        mid=(l+u)//2
        if lis1[mid]==item:
            print("found")
            return
        elif lis1[mid]<item:
            l=mid
        elif lis1[mid]>item:
            u=mid 
        else:
            print("not found")            



n=int(input("enter the size of list = "))

lis=[]

for i in range(n):

    ele=int(input())
    lis.append(ele)

item=int(input("enter the item to be searched = "))
lis1=sorted(lis)
print(lis1)
search(lis1,item)
