from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("350x500")
root.title("Login to system")


def registration():  # register user
    text = Label(text="To login to system you must be registered")
    text_user = Label(text="Enter your username: ")
    reg_user = Entry()
    text_password1 = Label(text="Enter your password: ")
    reg_password1 = Entry()
    text_password2 = Label(text="Password again: ")
    reg_password2 = Entry(show="*")
    button_reg = Button(text="Register", command=lambda: save())
    text.pack()
    text_user.pack()
    reg_user.pack()
    text_password1.pack()
    reg_password1.pack()
    text_password2.pack()
    reg_password2.pack()
    button_reg.pack()

    def save():  # save new user data
        file = "login.txt"
        if file:
            f = open("login.txt", "rb")
            read = pickle.load(f)
            f.close()
            if reg_user.get() in read:
                messagebox.showinfo("Oops", "Username already registered!")
            elif reg_password1.get() != reg_password2.get():
                messagebox.showinfo("Error", "Passwords doesn't match!")
            else:
                login_pass_save = {reg_user.get(): reg_password1.get()}
                f = open("login.txt", "wb")
                pickle.dump(login_pass_save, f)
                f.close()
                login()


def login():  # login user
    text_log = Label(text="Congratulations! You are registered. \n You can login now.")
    text_user = Label(text="Enter your username: ")
    log_user = Entry()
    text_password = Label(text="Enter your password: ")
    log_password = Entry(show="*")
    button_log = Button(text="Login", command=lambda: log_pass())
    text_log.pack()
    text_user.pack()
    log_user.pack()
    text_password.pack()
    log_password.pack()
    button_log.pack()

    def log_pass():  # check if username and password is correct
        f = open("login.txt", "rb")
        read = pickle.load(f)
        f.close()
        if log_user.get() in read:
            if log_password.get() == read[log_user.get()]:
                messagebox.showinfo("You have logged in", "You have 5 unread messages")
            else:
                messagebox.showerror("Error", "You have entered invalid username or password!")
        else:
            messagebox.showerror("Error", "Invalid username")


registration()


root.mainloop()
