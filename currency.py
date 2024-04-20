print("To convert currency ")
rupees=float(input("Enter the rupees to be converted = "))
print("Convert "+str(rupees)+ " to ")
print("1. U.S. Dollar (USD) 2.European Euro (EUR) 3. Japanese Yen (JPY) 4. British Pound (GBP)")
print("5. Swiss Franc (CHF) 6. Bahamian Dollor(BSD) 7. Rubble(RUB)")
choice=int(input("enter your choice "))
match choice:
    case 1:
        usd=rupees*79.4263
        print("RUPEES IN U.S. Dollar (USD) = "+str(usd))
    case 2:
        eur=rupees*80.98
        print("RUPEES IN European Euro (EUR) = "+str(eur))
    case 3:
        jpy=rupees*0.59
        print("RUPEES IN Japanese Yen (JPY) = "+str(jpy))
    case 4:
        gbp=rupees*95.93
        print("RUPEES IN British Pound (GBP) = "+str(gbp))
    case 5:
        chf=rupees*83.69
        print("RUPEES IN Swiss Franc (CHF) = "+str(chf))   
    case 6:
        bsd=rupees*79.63
        print("RUPEES IN Bahamian Dollor(BSD) = "+str(bsd)) 
    case 7:
        rub=rupees*1.33
        print("RUPEES IN  Rubble(RUB) = "+str(rub))
    case default:
        print("Invalid choice")                        