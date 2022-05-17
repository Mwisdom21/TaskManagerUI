import os

accepted = False
def accept():
    global accepted
    accepted = True
def login(name,password):
    success = False
    file = open("user_credentials.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        accept()
    else:
        print("wrong user name or password")
        
def register(name,password):
    file = open("user_credentials.txt","a")
    file.write("\n"+name+","+password)
    accept()
def access(option):
    global name
    if(option=="login"):
        name = input("Enter name: ")
        password = input("Enter password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter name: ")
        password = input("Enter password: ")
        register(name,password)

def begin():
    global option
    print("Welcome to HU Task Manager")
    option = input("Login or Register (Login,Reg): ")
    if(option!="login" and option!="register"):
        begin()
        
begin()
access(option)

if(accepted):
    print("Welcome to HU Task Manager")
    print("### USER CREDENTIALS ###")
    print("Username: ",name)
    
    print("Would you like to open HU Task Manager?")
    option = input("(Enter yes or no): ")
    if(option=="yes"):
        os.system("python mwphase5.py")
        print("Skiid")

