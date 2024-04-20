print(" 1.python  2.['monica','chandler','joey','ross'] 3.[3,5,6,7,2,9] ")
value=int(input("enter the choice = "))
match value:
    case 1:
        for item in 'python':
            print(item)
          
    case 2:
        for item in ["monica","chandler","joey","ross"]:
            print(item)
    
    case 3:
        for item in [3,5,6,7,2,9]:
            print(item)
        
    case default:
        print("invalid choice")

