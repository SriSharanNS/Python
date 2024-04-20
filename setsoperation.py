set1={"tokyo","denver","paris","brazil"}
set2={"dubai","tokyo","brazil","new york"}
print(set1)
print(set2)
print("1.intersection 2.union 3.difference")
choice=int(input("enter the choice "))
match choice:
    case 1:
        print(set1.intersection(set2))
    case 2:
        print(set1.union(set2))
    case 3:
        print(set1.difference(set2))   
    case default:
        print("invalid choice")     

 
