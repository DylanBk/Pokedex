# IMPORTS
from tkinter import *
import customtkinter

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
        #command=
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
    sign_up_window = Tk()
    width = sign_up_window.winfo_screenwidth()
    height = sign_up_window.winfo_screenwidth()
    sign_up_window.geometry("%dx%d" % (width, height))
    sign_up_window["bg"] = "red"

    sign_up_frame = Frame(sign_up_window)
    sign_up_frame.pack(side=LEFT)

    sign_up_password_entry = "0" # allows loop to begin without undefined variables error
    sign_up_password_confirm_entry ="1"

    while len(str(sign_up_password_entry)) < 8 and sign_up_password_entry != sign_up_password_confirm_entry:
        sign_up_username_label = Label(
            sign_up_window,
            text="Create a username: ",
            font=('Roboto', 12),
            bg="#89E7FF"
            )
        sign_up_username_label.place(x=(width/2-width/10), y=150, anchor=W)
        sign_up_username_entry = Entry(sign_up_window)
        sign_up_username_entry.place(x=(width/2-width/10), y=175, anchor=W)
 
        username = sign_up_username_entry.get()

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

        sign_up_button1 = customtkinter.CTkbutton(
            sign_up_window,
            text="Sign Up",
            #command=
        )
        sign_up_button1.place(x=(width/2-width/10), y=350, anchor=W)

        if len(str(sign_up_password_entry))  < 8:
            print("Your password must be longer than 8 characters")
            continue
        if sign_up_password_entry != sign_up_password_confirm_entry:
            print("Passwords don't match, please try again")
    
    # display_name_label = Label(
    #     sign_up_window,
    #     text="Create a display name: ",
    #     font=('Roboto', 12),
    #     bg="#89E7FF"
    # )
    # display_name_label.place(x=(width/2-width/10), y=350, anchor=W)
    # display_name_entry = Entry(sign_up_window)
    # display_name_entry.place(x=(width/2-width/10), y=375, anchor=W)

    sign_up_window.mainloop()





# MAIN LOOP
intial_window()
open_sign_up_window()
