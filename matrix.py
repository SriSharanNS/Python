matrix=[[1,2,3],
       [4,5,6],
       [7,8,9]]
print(matrix)
while(bool):
    print("1.display particular element 2.display particular row")
    choice=int(input("enter the choice = "))
    match choice:
            case 1:
                print(matrix[0][1])
            case 2:
                print(matrix[0])
            case default:
                print("invalid choice") 
    print("do u want to continue")
    value=input("press y or Y if u want to continue = ")
    value=value.upper()
    if value=='Y':
        bool=True
    else:
        bool=False
print("Thank You")        
         

               