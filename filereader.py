file =  open("text.txt","r")
for line in file.readlines():
    print(line[1:-1])
file.close()
