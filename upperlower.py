while True:
            print("1.upper case to lower case  2.lower case to upper case ")
            choice=int(input("enter the choice= "))
            match choice:
                    case 1:
                        lw=input("enter the text in upper case= ")
                        print("text in lower case= "+str(lw.lower()))
                    case 2:
                        up=input("enter the text in lower case= ")
                        print("text in upper case= "+str(up.upper()))
                        
                    case default:
                        print("invalid choice")
                        break    