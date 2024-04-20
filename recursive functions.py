print("1.function without parameters 2.function with one parameter 3.function with multiple parameters 4.function with keyword parameter")
choice=int(input("enter the choice = "))
match choice:
    case 1:
            def greet():
                print("hi")
                print("nice to meet you")
            print("Good Morning")
            greet()
            print("hope you are doing great")
    case 2:
            def greetpara(name):
                print("hi "+name)
                print("nice to meet you")
            print("Good Morning") 
            greetpara("joey")
            print("hope you are doing great") 
    case 3:
            def greetmultipara(name,age):
                print("hi "+name)
                print("your age is "+str(age))
            print("Good Morning")
            greetmultipara("ross",35)
            print("hope you are doing great")
    case 4:
            def greetkeypara(fname,lname):
                print("hi")
                print("first name is "+fname+" and last name is "+lname)
            print("Good Morning")
            greetkeypara(lname="tribiyani",fname="joey")
            print("hope you are doing great")  

    case default:
        print("invalid choice")            
