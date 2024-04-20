import calendar
from email.policy import default
c=calendar.TextCalendar(calendar.SUNDAY)

while True:
        mon=int(input("ENTER THE MONTH NUMBER = "))
        match mon:
            case 1:
                str=c.formatmonth(2022,1)
            case 2:
                str=c.formatmonth(2022,2)
            case 3:
                str=c.formatmonth(2022,3)
            case 4:
                str=c.formatmonth(2022,4)
            case 5:
                str=c.formatmonth(2022,5)
            case 6:
                str=c.formatmonth(2022,6)
            case 7:
                str=c.formatmonth(2022,7)
            case 8:
                str=c.formatmonth(2022,8)
            case 9:
                str=c.formatmonth(2022,9)
            case 10:
                str=c.formatmonth(2022,10)
            case 11:
                str=c.formatmonth(2022,11)
            case 12:
                str=c.formatmonth(2022,12)
            case default:
                print("INVALID MONTH")
                break
                
            
        print(str)                                                     


