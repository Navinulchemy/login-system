def create():
    users_db=open("users.TXT","r")
    username=input("create a username : ")
    password=input("create a password : ")
    password1=input("re-enter your password : ")

    SpecialSym = ['$', '@', '#', '%']
    uform=["@"]
    value = True
    u=[]
    p=[]

    for i in users_db:
     x, y = i.split(",")
     y = y.strip()
     u.append(x)
     p.append(y)

    if password != password1:
        print("your passwords don't match,retry once again")
        quit()

    else:
        if len(password)<5:
            print("password is too short")
            quit()



         elif len(password) > 16:
             print("password exceeds max length")
             quit()



         elif not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            quit()



         elif not any(char.isupper() for char in password):
           print('Password should have at least one uppercase letter')
           quit()



         elif not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            quit()



         elif not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#')
            quit()



    if username in u:
         print("the username already exists try another name")
         value=False


    else:

        try:
            v = (username.index("@") + 1)
            if username[0] == ("@" or "#" or "$" or '&'):
             print("username should not start with special symbols eg: @, #, $, &")
             quit()
            elif "@" not in username:
             print('username must have @ followed by your name as per your wish')
             quit()
            elif "." not in username:
                print("username must have . eg: nav@yahoo.com")
                quit()

            elif username[v] == ".":
             print("username cannot have   .  followed by @ / eg:ravi@123.com")
             quit()
        except:
            print("user name format error//example: raghu@gmail.com")


    if value:
        users_db=open("users.TXT","a")
        users_db.write(username+", "+password+"\n")
        print("account created successfully")
def log_in():
    username=input("enter username : ")
    password=input("enter your password : ")
    users_db=open("users.TXT","r")
    u = []
    p = []
    if len(username or password)>0:
     for i in users_db:
        x, y = i.split(",")
        y = y.strip()
        u.append(x)
        p.append(y)
    data = dict(zip(u, p))
    try:
        if data[username]:
            try:
                if password == data[username]:
                    print("login success")
                else:
                    print("password is incorrect ")
                    q = '''1.try again // 2.forget password'''
                    print(q)
                    fp=input("enter your choice : ")
                    if "1" in fp:
                     log_in()
                    elif "2" in fp:
                        result=0
                        passwd=data[username]
                        print("enter any 3 characters from your password to retrieve your password")
                        c1 = input("enter character 1 : ")
                        c2 = input("enter character 2 : ")
                        c3 = input("enter character 3 : ")
                        check=[c1, c2, c3]
                        for i in check:
                            if i in passwd:
                                result += 1
                        if result == 3:
                            print("retreiving your password pls waittt...")
                            print(f"The password of your account is {passwd}")
                    else:
                        print("invalid option")




            except:
                print("username or password is incorrect")
        else:
            print("username doesn't exist ")

    except:
        print("login error")
        print("please create an account to have access ")

choice=input("create|login : ")
if "create" in choice:
    create()
elif "login" in choice:
    log_in()
else:
    print("invalid input")








