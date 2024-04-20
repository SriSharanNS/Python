list1=[4,9,1,16,7,12]
list2=["monica","ross","chandler","rachel","phobe","joey",]
print(list1)
print(list2)
print("1.sort 2.reverse_sort 3.replace the element 4.min 5.max 6.sum 7.join and split")
choice=int(input("enter the choice = "))
match choice:
    case 1:
        print("to sort the list1 and list2")
        print(sorted(list1))
        print(sorted(list2))
    case 2:
        print("to reverse the sorted list")
        list1.sort(reverse=True)
        print(list1)
        list2.sort(reverse=True)
        print(list2)
    case 3:
        print("to replace an element")
        list1[0]=3
        list2[0]="emma" 
        print(list1)
        print(list2)   
    case 4:
        print("to find the min element")
        print(min(list1)) 
        print(min(list2))
    case 5:
        print("to find the max element") 
        print(max(list1)) 
        print(max(list2))  
    case 6:
        print("to sum of elements")
        print(sum(list1))
    case 7:
        c="-".join(list2)
        print(c) 
        sp=c.split(' - ')
        print(sp)  
        
    case default:
        print("invalid choice")           