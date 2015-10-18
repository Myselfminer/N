import translate, command
while 1:
    b=raw_input(">>>")
    a=open("console.txt","w")
    a.write(b)
    a.close()
    print(command.run(b))
