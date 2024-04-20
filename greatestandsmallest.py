print("To find greatest and smallest element")
num=[3,67,499,378,89,99]
list1=['chandler','ross','zodopia']
print(num)
print(list1)
print("1.greatest 2.smallest")
choice=int(input("enter the choice = "))
match choice:
    case 1:
        print("1.numbers 2.strings")
        value=int(input("enter the choice = "))
        if value==1:
            num=[3,67,499,378,89,99]
            max=num[0]
            for item in num:
              if item>max:
                 max=item
            print(max)
        elif value==2:
            list1=['chandler','ross','zodopia']
            max1=list1[0]
            for item in list1:
               if item>max1:
                max1=item
            print(max1) 
        else:
            print("invalid choice")   
    case 2:
        print("1.numbers 2.strings")
        value=int(input("enter the choice = "))
        if value==1:
            num=num=[3,67,499,378,89,99]   
            min=num[0]
            for item in num:
                if item<min:
                    min=item
            print(min)
        elif value==2:
            list1=['chandler','ross','zodopia']
            min=list1[0]
            for item in list1:
                if item<min:
                    min=item
            print(min)
        else:
            print("invalid choice")
    case default:
        print("invalid choice")                    

