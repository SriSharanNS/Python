print("1.display numbers within given range 2.display numbers in skip format")
choice=int(input("enter the choice = "))
if choice==1:
    rg=int(input("enter the range = "))
    for item in range(rg):
      print(item)
elif choice==2:
    print("range specified is [10,20] with 2 difference")
    for item in range(10,20,2):
        print(item)
else:
    print("invalid choice")        
