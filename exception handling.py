print("1.value error exception 2.arithematic exception")
choice=int(input("enter the choice = "))
match choice:
    case 1:
            try:
                age=int(input("enter the age = "))
                print("age = "+str(age))
            except ValueError:
                print("invalid age")
    case 2:
            try:
                age=int(input("enter the age = "))
                income=200000
                print("risk  = "+str(income/age))
            except ValueError:
                print("invalid age")    
            except ZeroDivisionError:
                print("age cannot be zero")
    case default:
        print("invalid choice")                 