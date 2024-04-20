def search(list,item):
    for i,ele in enumerate(lis):
        if ele==item:
            print("found")
            print("pos = "+str(i))
            return
    print("not found")        


n=int(input("enter the size of list = "))

lis=[]

for i in range(n):

    ele=int(input())
    lis.append(ele)

item=int(input("enter the item to be searched = "))
print(lis)
search(lis,item)

