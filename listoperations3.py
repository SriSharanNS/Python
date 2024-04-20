list1=[1,3,6,3,8,5,9]
print(list1)
print("1.index of element   2.check if elemnet is present in list 3.display every element in the list 4.index and element")
choice=int(input("enter the choice "))
match choice:
         case 1:
            print(list1.index(9))
         case 2:
            print(18 in list1)
         case 3:
            for item in list1:
                print(item)
         case 4:
            for index,ele in enumerate(list1):
              print(index,ele)
