print("1.addition 2.subtraction 3.multipication 4.division 5.modulus")
choice=int(input("enter the choice= "))
match choice:
    case 1:
           print("performing addition")
           a=float(input("enter the first number= "))
           b=float(input("enter the second number= "))
           sum=a+b
           print("sum is= "+str(sum))
    case 2:
           print("performing subtraction")
           a=float(input("enter the first number= "))
           b=float(input("enter the second number= "))
           sub=a-b
           print("difference= "+str(sub))
    case 3:
           print("performing multipication")
           a=float(input("enter the first number= "))
           b=float(input("enter the second number= "))             
           product=a*b
           print("product= "+str(product))
    case 4:
           print("performing division")
           a=float(input("enter the first number= "))
           b=float(input("enter the second number= "))
           if b>0:
            div=a/b
            print("divison= "+str(div))
           else :
            print("division not possible")
            
    case 5:
           print("performing modulus")
           a=float(input("enter the first number= "))
           b=float(input("enter the second number= ")) 
           mod=a%b
           print("modulus= "+str(mod))
    case default:
           print("invalid choice") 

