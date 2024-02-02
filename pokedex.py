# IMPORTS
from tkinter import *
import customtkinter
import time

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# STARTUP PAGE
def intial_window():

    root = Tk()
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root["bg"] = "red"

    welcome_label = Label(
        root,
        text ="-- Welcome to the Pokedex --",
        font=('Roboto', 50, 'bold'),
        bg = "#89E7FF"
    )
    welcome_label.place(x=(width/2), y=100, anchor=CENTER)

    login_options_frame = Frame(root)
    login_options_frame.pack(side=TOP) 

    login_button = customtkinter.CTkButton(
        root,
        text ="Login",
        command=open_login_window
    )
    login_button.pack(pady=150)

    sign_up_button = customtkinter.CTkButton(
        root,
        text ="Sign Up",
        command=open_sign_up_window
    )
    sign_up_button.place(x=(width/2), y=200, anchor=CENTER)

    forgot_password_button = customtkinter.CTkButton(
        root,
        text ="Forgotten your password?",
    )
    forgot_password_button.place(x=(width/2), y=235, anchor=CENTER)

    root.mainloop()

# SIGN UP WINDOW
def open_sign_up_window():

     # SET UP ACCOUNT
    def signUp():
        global username, password, password_confirm, display_name

        username = sign_up_username_entry.get()
        password = sign_up_password_entry.get()
        password_confirm = sign_up_password_confirm_entry.get()

        if username == "":
            error_label.config(text="Username cannot be blank")
        elif len(str(password)) < 8:
            error_label.config(text="Your password must be longer than 8 characters")
        elif password != password_confirm:
            error_label.config(text=("Passwords don't match, please try again"))
        else:
            sign_up_username_label.destroy()
            sign_up_username_entry.destroy()
            sign_up_password_label.destroy()
            sign_up_password_entry.destroy()
            sign_up_password_confirm_label.destroy()
            sign_up_password_confirm_entry.destroy()
            error_label.destroy()
            sign_up_button.destroy()

            set_display_name_label = Label(
                sign_up_window,
                text="Choose your display name",
                font=('Roboto', 12),
                bg = "#89E7FF"
            )
            set_display_name_label.place(x=(width/2-width/10), y=150, anchor=W)
            set_display_name_entry = Entry(sign_up_window)
            set_display_name_entry.place(x=(width/2-width/10), y=175, anchor=W)

            display_name = set_display_name_entry.get()


    sign_up_window = Tk()
    width = sign_up_window.winfo_screenwidth()
    height = sign_up_window.winfo_screenwidth()
    sign_up_window.geometry("%dx%d" % (width, height))
    sign_up_window["bg"] = "red"

    sign_up_frame = Frame(sign_up_window)
    sign_up_frame.pack(side=LEFT)

    sign_up_username_label = Label(
        sign_up_window,
        text="Create a username: ",
        font=('Roboto', 12),
        bg="#89E7FF"
        )
    sign_up_username_label.place(x=(width/2-width/10), y=150, anchor=W)
    sign_up_username_entry = Entry(sign_up_window)
    sign_up_username_entry.place(x=(width/2-width/10), y=175, anchor=W)

    sign_up_password_label = Label(
        sign_up_window,
        text="Create a password (must be atleast 8 characters long) : ",
        font=('Roboto', 12),
        bg="#89E7FF"
    )
    sign_up_password_label.place(x=(width/2-width/10), y=200, anchor=W)
    sign_up_password_entry = Entry(sign_up_window)
    sign_up_password_entry.place(x=(width/2-width/10), y=225, anchor=W)

    sign_up_password_confirm_label = Label(
        sign_up_window,
        text="Confirm your password: ",
        font=('Roboto', 12),
        bg="#89E7FF"
    )
    sign_up_password_confirm_label.place(x=(width/2-width/10), y=250, anchor=W)
    sign_up_password_confirm_entry = Entry(sign_up_window)
    sign_up_password_confirm_entry.place(x=(width/2-width/10), y=275, anchor=W)

    sign_up_button = customtkinter.CTkButton(
        sign_up_window,
        text="Sign Up",
        command= signUp
    )
    sign_up_button.place(x=(width/2-width/10), y=350, anchor=W)

    error_label = Label(
        sign_up_window,
        foreground = "red",
        command=error_label.hide_label
    )
    error_label.place(x=(width/2-width/10), y=390, anchor=W)


    sign_up_window.mainloop()

def open_login_window():

    def login():
        pass

    login_window = Tk()
    width = login_window.winfo_screenwidth()
    height = login_window.winfo_screenwidth()
    login_window.geometry("%dx%d" % (width, height))
    login_window["bg"] = "red"

    login_username_label = Label(
        login_window,
        text="Enter username: ",
        font=('Roboto', 12),
        bg="#89E7FF"
    )
    login_username_label.place(x=(width/2-width/10), y=150, anchor=W)
    login_username_entry = Entry(login_window)
    login_username_entry.place(x=(width/2-width/10), y=175, anchor=W)

    login_password_label = Label(
        login_window,
        text="Enter password: ",
        font=('Roboto', 12),
        bg="#89E7FF"
    )
    login_password_label.place(x=(width/2-width/10), y=200, anchor=W)
    login_password_entry = Entry(login_window)
    login_password_entry.place(x=(width/2-width/10), y=225, anchor=W)

    login_button = customtkinter.CTkButton(
        login_window,
        text="Log in",
        command=login
    )





# MAIN LOOP
intial_window()