str = "Hello <<UserName>>, How are you?"
name= input("Enter your name: ")
if len(name) < 3:
    print('min name length is 3 characters')
else:
    str = str.replace("<<UserName>>",name)
    print(str)
