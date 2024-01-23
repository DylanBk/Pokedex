# IMPORTS
from tkinter import *
import customtkinter

# DEFINING INITAL WINDOW
root = Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root["bg"] = "red"

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# LOGIN PAGE
welcomeLabel = Label(
    root,
    text ="-- Welcome to the Pokedex --",
    font=('Times New Roman', 50, 'bold'),
    bg = "#89E7FF"
)
welcomeLabel.place(x=(width/2), y=100, anchor=CENTER)

loginOptionsFrame = Frame(root)
loginOptionsFrame.pack(side=TOP) 

loginButton = customtkinter.CTkButton(
    root,
    text ="Login",
)
loginButton.pack(pady=150)

signupButton = customtkinter.CTkButton(
    root,
    text ="Sign Up",
)
signupButton.place(x=(width/2), y=200, anchor=CENTER)

forgotPwButton = customtkinter.CTkButton(
    root,
    text ="Forgotten your password?",
)
forgotPwButton.place(x=(width/2), y=235, anchor=CENTER)


root.mainloop()