from cryptography.fernet import Fernet
import os

main_pwd = input("Enter your Passaword manager Password: ")

def key_generator():
    key = Fernet.generate_key()
    f = open("key.key","wb")
    f.write(key)
    f.close()
    
def key_lead():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

if not os.path.exists("key.key"):
    key_generator()
else:
    pass

key = key_lead()
token = Fernet(key)


def view():
    with open("passwords", "r") as f:
        for lines in f.readlines():
            uname,passw = lines.split("|")
            passwo = token.decrypt(passw.encode()).decode()
            print(f"Username: {uname} & Password: {passwo}")
               
def add():
    name = input("Enter Username: ")
    password =  input("Enter Password: ")
    with open("passwords", "a") as f:
        passwo = token.encrypt(password.encode()).decode()
        f.write(f"{name}|{passwo} \n")


while True:
    mode = input("Do you want to view or add passwords? or wanna quit?(view/add/q): ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid Query!")
        
        
        
        