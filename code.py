import re
def register():
    db=open(r"C:\Users\bharath.g\Desktop\database.txt","r")
    email_condition='[a-z]*@[a-z]*.[a-z]{2,3}'
    EmailID=input("Create a EmailID:")
    if re.search(email_condition,EmailID):
        print('Right Email')
    else:
        print('Wrong Email')
    flag=0
    password=input("Create a password:")
    if not re.search('[a-z]',password):
        flag=1
    if not re.search('[0-9]',password):
        flag=1
    if not re.search('[A-Z]',password):
        flag=1
    if not re.search('[&@#%*!]',password):
        flag=1
    if len(password)>=5 and len(password)<16:
        flag=0
        
    if (flag==0):
        print("password is valid")
    else:
        print("password is invalid")
        
    db=open(r"C:\Users\bharath.g\Desktop\database.txt","a")
    db.write(EmailID+","+password+"\n")
    print("Success!")
    db.close()
    
def login():
    EmailID=input("Enter Email/Username:")
    password=input("Enter password:")
    db= open(r"C:\Users\bharath.g\Desktop\database.txt",'r')
    read_obj=db.readlines()
    for i in read_obj:
        i=i.strip('\n')
        info=i.split(',')
        if EmailID==info[0] and password==info[1]:
            print("Login Successfully")
            break
        else:
            print("EmailId and password wrong please Register!!!!")
    
    db.close()
    
            
            
def forget_password():
    email=input("Enter EmailID:")
    db=open(r"C:\Users\bharath.g\Desktop\database.txt","r")
    file_content=db.readlines()
    for i in file_content:
        i=i.strip('\n')
        x=i.split(',')
        if email==x[0]:
            print(x[1])
            break
        else:
            print("EmailID is not register go and Register!!!")
        
db.close()
    
while 1:
    print("*** Login System ***")
    print("1.Register")
    print("2.Login")
    print("3.Forget Password")
    print("4.Exit")
    ch = int(input(" Enter your choice : "))
    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        forget_password()
    elif ch == 4:
        break
    else:
        print(" \n Wrong Choice! \n ")
    
