import random
import string

print("1.upper case 2.lower case 3.entire string")
choice=int(input("enter the choice = "))
match choice:
    case 1:
        print(random.choice(string.ascii_uppercase))
    case 2:
        print(random.choice(string.ascii_lowercase))
    case 3:
        print(string.ascii_letters)
    case default:
        print("invalid choice")          

