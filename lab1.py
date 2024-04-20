print("to calculate gross pay ")
b_pay=float(input("enter the basic pay: " ))
h_all=float(input("enter the house rent allowence in percentage: "))
h_all=(h_all/100)
h_rent=h_all*b_pay
gross=h_rent+b_pay
if gross<=2000:
    tax=0
    print("no tax")
elif gross>2000 and gross<=4000:
    tax=0.03*gross
    print("tax is "+str(tax)) 
elif gross>4000 and gross<=5000:
    tax=0.05*gross
    print("tax is "+str(tax))
else:
    tax=0.08*gross
    print("tax is "+str(tax))   
print("house rent is "+str(h_rent))
print("gross is "+str(gross))
print("total salary is "+str(gross-tax))               

                