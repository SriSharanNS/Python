print("list of subjects")
while True:
              print("1.student_1 2.student_2 3.student_3")
              choice=int((input("enter the choice = ")))
              match choice:
                            case 1:
                                   print("subjects of student 1")
                                   list1=["geo","his","math","soc"]
                                   print(list1)
                                   print(len(list1))
                            case 2:
                                   print("subjects of student 2")
                                   list2=["sports","math","chem",]
                                   print(list2)
                                   print(len(list2))
                            case 3:
                                   print("subjects of student 3")
                                   list3=["python","java"] 
                                   print(list3)
                                   print(len(list3))
                            case default:
                                   print("invalid choice")
                                   break                  