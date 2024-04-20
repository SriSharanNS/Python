emoji={  "1":"Good Morning 😀",
         "2":"Good Afternoon 😁",
         "3":"Good Evening 😃",
        
}
em=input("enter the value = ")
output=""
for item in em:
    output+=emoji.get(item)+" "
print(output)    