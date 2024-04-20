secretno=7;
i=0;
while i<3:
    guess=int(input("enter the secret number = "))
    i+=1;
    if guess==secretno:
        print("you won")
        break;
else:        
    print("you lost")        
