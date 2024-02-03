# IMPORTS
from tkinter import *
import customtkinter
import random

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# STARTUP PAGE
def intial_window(): #inital window containing options to login, signup, and forgotten password

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

    login_button = customtkinter.CTkButton(
        root,
        text ="Login",
        command=open_login_window
    )
    login_button.place(x=(width/2), y=215, anchor=CENTER)

    sign_up_button = customtkinter.CTkButton(
        root,
        text ="Sign Up",
        command=open_sign_up_window
    )
    sign_up_button.place(x=(width/2), y=250, anchor=CENTER)

    forgot_password_button = customtkinter.CTkButton(
        root,
        text ="Forgotten your password?",
        command=open_forgot_password_window
    )
    forgot_password_button.place(x=(width/2), y=300, anchor=CENTER)

    root.mainloop()

# SIGN UP WINDOW
def open_sign_up_window(): #subroutine for signing up for a pokedex account

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
                bg="#89E7FF"
            )
            set_display_name_label.place(x=(width/2-width/10), y=150, anchor=W)
            set_display_name_entry = Entry(sign_up_window)
            set_display_name_entry.place(x=(width/2-width/10), y=175, anchor=W)

            display_name = set_display_name_entry.get()

            sequence_samples = ["3u4tvnyc3579cqnyc3mc", "64s8dh7428h72vsh72sr7ha", "66v4h2ht4svrhve8tsae"]
            sequence_unmixed = random.choice(sequence_samples)
            sequence_mixed = ''.join(random.choices(sequence_unmixed, k=15))
            ACCOUNT_ID = sequence_mixed
            print(ACCOUNT_ID)

            account_id_label = Label(
                sign_up_window,
                text=(f"This is your account ID {ACCOUNT_ID}, treat it as you would your password."),
                font=('Roboto', 12),
                bg="#89E7FF",
                fg="red"
            )
            account_id_label.place(x=(width/2-width/10), y=250, anchor=W)

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
        command=signUp
    )
    sign_up_button.place(x=(width/2-width/10), y=350, anchor=W)

    error_label = Label(
        sign_up_window,
        foreground = "red",
        # command=error_label.hide_label #find a way to only show when needed
    )
    error_label.place(x=(width/2-width/10), y=390, anchor=W)

    sign_up_window.mainloop()


# LOGIN WINDOW
def open_login_window(): #subroutine for logging into pokedex account

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
    login_button.place(x=(width/2-width/10), y=300, anchor=W)


# FORGOT PASSWORD
def open_forgot_password_window(): #subroutine for password recovery

    def forgot_password():
        # if username and account id match then return password
        pass

    forgot_pw_window = Tk()
    width = forgot_pw_window.winfo_screenwidth()
    height = forgot_pw_window.winfo_screenheight()
    forgot_pw_window.geometry("%dx%d" % (width, height))
    forgot_pw_window["bg"] = "red"

    forgot_pw_username_label = Label(
        forgot_pw_window,
        text="Enter Username",
        font=('Roboto', 12),
        bg="#89E7FF"
    )
    forgot_pw_username_label.place(x=(width/2-width/10), y=150, anchor=W)
    forgot_pw_username_entry = Entry(forgot_pw_window)
    forgot_pw_username_entry.place(x=(width/2-width/10), y=175, anchor=W)

    forgot_pw_account_id_label = Label(
        forgot_pw_window,
        text="Enter Account ID",
        font=('Roboto', 12),
        bg="#89E7FF"
    )
    forgot_pw_account_id_label.place(x=(width/2-width/10), y=200, anchor=W)
    forgot_pw_account_id_entry = Entry(forgot_pw_window)
    forgot_pw_account_id_entry.place(x=(width/2-width/10), y=225, anchor=W)

    forgot_pw_button = customtkinter.CTkButton(
        forgot_pw_window,
        text="Recover Password",
        command=forgot_password
    )
    forgot_pw_button.place(x=(width/2-width/10), y=300, anchor=W)


# MAIN LOOP
intial_window()