print("1.square 2.cube")
choice=int(input("enter the choice = "))
match choice:
    case 1:
        def square(num):
            return(num*num)
        result=square(3)
        print("result = "+str(result))
    case 2:
        def cube(num):
            print("result = "+str(num*num*num))
        cube(2)
    case default:
        print("invalid choice")                