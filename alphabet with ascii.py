import random

print("1.upper case alphabets 2.lower case alphabets")
choice=int(input("enter the choice = "))
match choice:
    case 1:
        r=random.randrange(65,90)
        print((r,chr(r)))
    case 2:
        r=random.randrange(97,122)
        print((r,chr(r)))    
    case default:
        print("invalid choice")    