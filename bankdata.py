print("welcome to bank")
name=input("enter your name = ")
num=int(input("enter the no = "))
bal=0
print("1.check balance 2.deposit amount 3.withdraw amount ")
choice=int(input("enter your choice = "))
match choice:
       case 1:
        print(f"balance= {bal}")
       case 2:
        damount=int(input("enter the amount to be deposited = "))
        bal=bal+damount
        print("balance= "+str(bal))
       case 3:
        wamount=int(input("enter the amount to be withdrawed = "))
        if wamount<bal:
            bal=bal-wamount
            print("balance = "+str(bal))
       case default:
        print("invalid choice")   