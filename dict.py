customer={ "name":"joey tribiyani",
            "age":30,
            "address":"4th street , central perk ,north avenue",
             "phone": 1536329833
         }
print("1.display all details 2.display only name 3.display only age 4.display only address 5.display only phone number ")
choice=int(input("enter your choice = "))
match choice:
    case 1:
        print(customer)
    case 2:
        print("name = "+str(customer["name"]))
    case 3:
        print("age = "+str(customer["age"]))
    case 4:
        print("address = "+str(customer["address"]))
    case 5:
        print("phone number = "+str(customer["phone"]))
    case default:
        print("invalid choice")                             