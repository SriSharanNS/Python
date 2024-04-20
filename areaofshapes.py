print("To find area of shapes")
while True:
    print("1.rectangle 2.circle 3.triangle 4.square")
    choice=int(input("enter the choice= "))
    if choice==1:
        print("To find area of rectangle")
        len=float(input("enter the length= "))
        brd=float(input("enter the breadth= "))
        area =len*brd
        print("the area is= "+str(area)+" sq units")
    elif choice==2:
        print("To find area of circle")
        rad=float(input("enter the radius= "))
        area=3.14*rad*rad
        print("the area is= "+str(area)+" sq units")
    elif choice==3:
        print("To find area of triangle")
        base=float(input("enter the base= "))
        hgt=float(input("enter the height= "))
        area=0.5*base*hgt
        print("the area is= "+str(area) +" sq units")
    elif choice==4:
        print("To find area of square")
        side=float(input("enter the side= "))
        area=side*side
        print("the area is =" +str(area)+" sq units") 
    else:
        print("invalid choice") 
        break         