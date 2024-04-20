name=input("enter the name = ")
size=len(name)
if size<3:
    print("name should contain atleast 3 characters")
elif size>=3 and size<50:
    print("name is good")
else:
    print("name should not exceed 50 characters")        