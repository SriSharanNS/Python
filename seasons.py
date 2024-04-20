print("1.summer 2.winter 3.rainy 4.spring")
choice=int(input("enter your choice = "))
match choice:
            case 1:
                   sum=["march","april","may","june"]
                   print(sum)
            case 2:
                   win=["july","auguest","september"]
                   print(win)
            case 3:
                   ra=["october","november","december"]
                   print(ra)
            case 4:
                   sp=["january","febraury"]
                   print(sp)   
            case default:
                   print("invalid choice")
                                             