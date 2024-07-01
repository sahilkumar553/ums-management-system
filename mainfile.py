from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Student Register")
    register_screen.geometry("980x720")
 
    global username
    global password
    global reg
    global address
    global reg_entry
    global address_entry
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    reg = StringVar()
    address = StringVar()
    
    Label(register_screen, text="Please enter the details below", bg="orange", width="300", height="2", font=("Britannic Bold", 18)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Name : ", font=("calibri", 13))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="").pack()
    reg_lable = Label(register_screen, text="Registration no.: ", font=("calibri", 13))
    reg_lable.pack()
    reg_entry = Entry(register_screen, textvariable=reg)
    reg_entry.pack()
    Label(register_screen, text="").pack()
    address_lable = Label(register_screen, text="Email address: ", font=("calibri", 13))
    address_lable.pack()
    address_entry = Entry(register_screen, textvariable=address)
    address_entry.pack()
    Label(register_screen, text="").pack()
    password_lable = Label(register_screen, text="New Password : ", font=("calibri", 13))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#00f000", font =("arial black",10), command = register_user).pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Close", command=delete_register_screen).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Account Login")
    login_screen.geometry("980x720")
    Label(login_screen, text="Please enter the credentials to login",bg="orange", width="300", height="2",font=("Britannic Bold", 18)).pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="\n Username(Name):", font=("calibri", 13)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password :", font=("calibri", 13)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="#00f000", font =("arial black",10),command = login_verify).pack()
    Label(login_screen, text="Or", font =("arial black" , 10)).pack()
    Label(login_screen, text="Don't have an Account", font =("arial black" , 10)).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Register", width=10, height=1, bg="#0fffff", font =("arial black",10),command = register).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Close", command=delete_login_screen).pack()
    
    
#designing window for new authority

def new_supervisor():
    global new_screen
    new_screen = Toplevel(main_screen)
    new_screen.title("New User Supervisor")
    new_screen.geometry("980x720")
 
    global username1
    global password1
    global uid1
    global address1
    global uid_entry1
    global address_entry1
    global username_entry1
    global password_entry1
    username1 = StringVar()
    password1 = StringVar()
    uid1 = StringVar()
    address1 = StringVar()
    
    Label(new_screen, text="Please enter the details below", bg="orange", width="300", height="2", font=("Britannic Bold", 18)).pack()
    Label(new_screen, text="").pack()
    username1_lable = Label(new_screen, text="Name : ", font=("calibri", 13))
    username1_lable.pack()
    username_entry1 = Entry(new_screen, textvariable=username1)
    username_entry1.pack()
    Label(new_screen, text="").pack()
    uid1_lable = Label(new_screen, text="UID: ", font=("calibri", 13))
    uid1_lable.pack()
    uid_entry1 = Entry(new_screen, textvariable=uid1)
    uid_entry1.pack()
    Label(new_screen, text="").pack()
    address1_lable = Label(new_screen, text="Email Address: ", font=("calibri", 13))
    address1_lable.pack()
    address_entry1 = Entry(new_screen, textvariable=address1)
    address_entry1.pack()
    Label(new_screen, text="").pack()
    password1_lable = Label(new_screen, text="New Password : ", font=("calibri", 13))
    password1_lable.pack()
    password_entry1 = Entry(new_screen, textvariable=password1, show='*')
    password_entry1.pack()
    Label(new_screen, text="").pack()
    Button(new_screen, text="Register", width=10, height=1, bg="#00f000", font =("arial black",10), command=new_user).pack()
    Label(new_screen, text="").pack()
    Button(new_screen, text="Close", command=delete_supervisor_screen).pack()
    
# Implementing event on new user student register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    reg_info= reg.get()
    address_info= address.get()
    
    list_of_files = os.listdir()
    if username_info in list_of_files:
        Label(register_screen, text="User already exist", fg="Red", font=("Arial Black", 20)).pack()
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(reg_info + "\n")
        file.write(address_info + "\n")
        file.write(password_info )
        file.close()

        username_entry.delete(0, END)
        reg_entry.delete(0, END)
        address_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(register_screen, text="Registration Success", fg="green", font=("Arial Black", 16)).pack()

    

#Implementing event on new user supervisor register button
def new_user():
    
    username_info = username1.get()
    password_info = password1.get()
    uid_info= uid1.get()
    address_info= address1.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(uid_info + "\n")
    file.write(address_info + "\n")
    file.write(password_info )
    file.close()
 
    username_entry1.delete(0, END)
    uid_entry1.delete(0, END)
    address_entry1.delete(0, END)
    password_entry1.delete(0, END)
 
    Label(new_screen, text="Registration Success", fg="green",font=("Arial Black", 16)).pack()

    

# Implementing event on login button 
def login_verify():
    global username2
    global password2
    username2 = username_verify.get()
    password2 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username2 in list_of_files:
        file1 = open(username2, "r")
        for last_line in file1:            #getting the last line that consist of password
            pass
        if password2 == last_line:
            login_success()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 

 # Designing popup for login success
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("700x550")
    Label(login_success_screen,  height="3", width="300" ,text="Login Success", bg="#0fffff",font=("Arial Black", 10)).pack()
    file1 = open(username2, "r")
    name = file1.readline()
    Label(login_success_screen, text="Name :", fg="black", font=("calibri", 14)).pack()
    Label(login_success_screen, text=name , fg="Green", font=("calibri", 14)).pack()
    reg_no = file1.readline()
    Label(login_success_screen, text="Registration no./UID(for supervisor) :" , fg="black", font=("Arial Black", 14)).pack()
    Label(login_success_screen, text=reg_no , fg="green", font=("calibri", 14)).pack()
    add=file1.readline()
    Label(login_success_screen, text="E mail", fg="black", font=("Arial Black", 14)).pack()
    Label(login_success_screen, text=add , fg="green", font=("calibri", 14)).pack()
    passwo=file1.readline()
    Label(login_success_screen, text="Password :", fg="black", font=("Arial Black", 14)).pack()
    Label(login_success_screen, text=passwo , fg="green", font=("calibri", 14)).pack()
    file1.close()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Close", command=delete_login_success).pack()

 
    
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Incorrect password")
    password_not_recog_screen.geometry("300x300")
    Label(password_not_recog_screen, height="2", width="300" ,text="Invalid Password", bg="#0fffff",font=("Arial Black", 14)).pack()
    Label(password_not_recog_screen, text="").pack()
    Label(password_not_recog_screen, text="Enter Correct Password!!", fg="red", font=("Arial Black", 12)).pack()
    Label(password_not_recog_screen, text="").pack()
    Button(password_not_recog_screen, text="Close", command=delete_password_not_recognised).pack()
 
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("User not found")
    user_not_found_screen.geometry("300x300")
    Label(user_not_found_screen, height="2", width="300" ,text="User Not Found", bg="#0fffff",font=("Arial Black", 14)).pack()
    Label(user_not_found_screen, text="").pack()
    Label(user_not_found_screen, text="Register first!!!", fg="red", font=("Arial Black", 12)).pack()
    Label(user_not_found_screen, text="").pack()
    Button(user_not_found_screen, text="Close", command=delete_user_not_found_screen).pack()
    
    
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_register_screen():
    register_screen.destroy()

def delete_new_supervisor_screen():
    new_screen.destroy()

def delete_login_screen():
    login_screen.destroy()

    
def delete_supervisor_screen():
    new_screen.destroy()
    

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("980x720")

    main_screen.title("UMS")
    Label(text="Lovely Professional University", bg="orange", width="300", height="2", font=("Algerian", 18)).pack()
    Label(text="\n\n\n\n\n").pack()
    Button(text="Login", height="2", width="25",bg="#0fffff",font=("Arial Black", 10), command = login).pack()
    Label(text="").pack()
    Button(text="New User", height="2", width="25",bg="#0fffff",font=("Arial Black", 10), command=register).pack()
    Label(text="").pack()
    Button(text="Request for Supervisor", height="2", width="25",bg="#0fffff",font=("Arial Black", 10), command=new_supervisor).pack()
    main_screen.mainloop()


 
 
main_account_screen()