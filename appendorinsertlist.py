list1=["geo","his","java","python"]
print(list1)
print("1.append 2.insert 3.extend 4.remove 5.pop 6.remove all elemnts")
choice=int(input("enter your choice = "))
match choice:
    case 1:
           print("to append an element")
           list1.append("art")
           print(list1)
    case 2:
        print("to insert an an element")
        list1.insert(2,"ds")
        print(list1)
    case 3:
        print("to extend the list")
        list2=["math","cs"]
        list1.extend(list2)
        print(list1) 
    case 4:
        print("to remove a element")
        list1.remove("java")
        print(list1)
    case 5:
        print("to pop only top element")
        popped=list1.pop()
        print(popped) 
        print(list1) 
    case 6:
        print("to remove all elements")
        list1.clear()
        print(list1)             
    case default:
        print("invalid choice")    