import opcode
import re
granted = False
def grant():
    global granted
    granted = True
def check(x):
    flag=0
    if not re.search('[a-z]',x):
        flag=1
    if not re.search('[0-9]',x):
        flag=1
    if not re.search('[A-Z]',x):
        flag=1
    if not re.search('[!@#$%^&*]',x):
        flag=1
    if len(x)<=5:
        flag=1
    if len(x)>=16:
        flag=1
    if (flag==0):
        print("REGISTRATION COMPLETED")
    else:
        print("NOT VALID")
        
def check_1(y):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex,y)):
        print("REGISTRATION COMPLETED")
    else:
        print("NOT VALID")
        
def login(user_id,password):
    success = False
    file=open("C:/Users/Rishi/Desktop/login&Reg/user_id_details.txt","r")
    for i in file:
        a,b=i.split(",")
        b=b.strip()
        if(a==user_id and b==password):
            success=True
            break
    file.close()
    if(success):
        print("****LOGIN SUCESSFUL!!!!!****")
        grant()
    else:
        print("WRONG USER_ID OR PASSWORD")
        
def register(user_id,password):
    if check_1(user_id) == "NOT VALID"  and check(password) == "NOT VALID":
        print("enter valid username and password")
    
    else:    
        file=open("C:/Users/Rishi/Desktop/login&Reg/user_id_details.txt","a")
        file.write("\n" +user_id+","+password)
        file.close()
        grant() 
        
def access(option):
    global user_id
    if(option=="login"):
        user_id = input("Enter your user_id: ")
        password = input("Enter your password: ")
        login(user_id,password)
    else:
        print("ENTER YOUR USER_ID AND PASSWORD TO REGISTRER")
        user_id = input("Enter your user_id: ")
        password = input("Enter your password: ")
        if check_1(user_id) == "NOT VALID"  and check(password) == "NOT VALID":
            print()
        else:    
            file=open("C:/Users/Rishi/Desktop/login&Reg/user_id_details.txt","a")
            file.write("\n" +user_id+","+password)
            file.close()
            grant() 
        register(user_id,password)
    
def begin():
    global option 
    print("WELCOME TO THE ****MANCHESTER UNITED CLUB****!!!!!")
    option = input("LOGIN OR REGISTRER (LOGIN,REGISTER): ")
    if(option!="login" and option!="register"):
        print("ENTER A VALID OPTION")
        begin()
        
begin()
access(option)

    
    