# IMPORTS
from tkinter import *
import customtkinter
import pandas as pd
import requests
import random

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


# CLOSE WINDOWS
def close_window(window): #destroys the window from which it is called from
    """

    ...Closes the window which is passed as an argument.
    
    Args:
        window (var): The window to be closed
    """
    window.destroy()

# TO LAST WINDOW
def to_prev_window(current, previous):#destroys current window and opens the previous window
    """
    ...Closes the current window and opens the previous window.

    Args:
        current (var): The window currently open.
        previous (func): The function which opens the previous window.
    """
    current.destroy()
    previous()

# ENCRYPT PW
def encrypt(password, key): #encrypts passwords, creates a key used to compare entered pw and stored pw
    """
    ...Encrypts a unicode input and returns the encrypted password as well as the key.

    Args:
        password (str): The string to be encrypted.
        key (int): If available, the key used to manipulate the encrpytion.

    Returns:
        enc_pw (str): The encrypted string.
        key(str): A key which can be used to compare enc_pw with user inputs.
    """
    if key is None:
        shift = random.randint(1,26)
        n = random.randint(1,9)
    else:
        shift = str(key)[:2]
        shift = int(shift)
        n = str(key)[-1]
        n = int(n)

    enc_pw = []

    for char in password:
        new_char = ord(char) + shift
        enc_pw.append(new_char)

    if shift < 10:
        shift = shift + 10

    enc_pw.append(shift)
    enc_pw = str(enc_pw).replace("[","")
    enc_pw = enc_pw.replace("]","")
    enc_pw = enc_pw.replace("'","")
    enc_pw = enc_pw.replace(",","")
    enc_pw = enc_pw.replace(" ","")

    enc_pw = int(enc_pw) * n
    enc_pw = str(enc_pw) + str(n)

    key = str(shift) + str(n)

    return enc_pw, key

# STARTUP PAGE
def intial_window(): #inital window containing options to login, signup, and forgotten password
    init_window = Tk()
    init_window.geometry("500x500")
    init_window["bg"] = "red"
    # init_window["bg"] = PhotoImage(file = "main-bg.png")

    welcome_label = Label(
        init_window,
        text="-  Welcome to the Pokedex  -",
        font=('Roboto', 28, 'bold'),
        bg="red",
        fg="white"
    )
    welcome_label.place(x=250, y=100, anchor=CENTER)

    login_button = customtkinter.CTkButton(
        init_window,
        text ="Login",
        command=lambda: [close_window(init_window), open_login_window()]
    )
    login_button.place(x=250, y=250, anchor=CENTER)

    sign_up_button = customtkinter.CTkButton(
        init_window,
        text ="Sign Up",
        command=lambda: [close_window(init_window), open_sign_up_window()]
    )
    sign_up_button.place(x=250, y=300, anchor=CENTER)

    # forgot_password_button = customtkinter.CTkButton(
    #     init_window,
    #     text ="Forgotten your password?",
    #     command=lambda: [close_window(init_window), open_forgot_password_window()]
    # )
    # forgot_password_button.place(x=200, y=300, anchor=CENTER)

    init_window.mainloop()

# SIGN UP WINDOW
def open_sign_up_window(): #subroutine for signing up for a pokedex account

     # SET UP ACCOUNT
    def signUp():
        global username

        username = sign_up_username_entry.get()
        password = sign_up_password_entry.get()
        password_confirm = sign_up_password_confirm_entry.get()

        if username == "":
            error_label.config(
                text="Username cannot be blank",
                bg="white",
                fg="red"
            )
        elif len(str(password)) < 8:
            error_label.config(
                text="Your password must be longer than 8 characters",
                bg="white",
                fg="red"
            )
        elif password != password_confirm:
            error_label.config(
                text="Passwords don't match, please try again",
                bg="white",
                fg="red"
            )
        else:
            sign_up_username_label.destroy()
            sign_up_username_entry.destroy()
            sign_up_password_label.destroy()
            sign_up_password_entry.destroy()
            sign_up_password_confirm_label.destroy()
            sign_up_password_confirm_entry.destroy()
            error_label.destroy()
            sign_up_button.destroy()

            enc_pw, key = encrypt(password, None)

            sequence_samples = ["3u4tvnyc3579cqnyc3mc", "64s8dh7428h72vsh72sr7ha", "66v4h2ht4svrhve8tsae"]
            sequence_unmixed = random.choice(sequence_samples)
            sequence_mixed = ''.join(random.choices(sequence_unmixed, k=15))
            ACCOUNT_ID = sequence_mixed
           
            user_data = {
                "Username": [username],
                "Password": [enc_pw],
                "userID": [ACCOUNT_ID],
                "key": [key]
            }
            df = pd.DataFrame(user_data)
            df.to_csv("userData.csv", header=False, index=False, mode="a")

            close_window(sign_up_window)

    sign_up_window = Tk()
    sign_up_window.geometry("500x500")
    sign_up_window["bg"] = "red"

    back_to_menu = customtkinter.CTkButton(
        sign_up_window,
        text="Back to menu",
        command=lambda: to_prev_window(sign_up_window, intial_window)
    )
    back_to_menu.place(x=30,y=30)

    sign_up_frame = Frame(sign_up_window)
    sign_up_frame.pack(side=LEFT)

    sign_up_username_label = Label(
        sign_up_window,
        text="Create a username: ",
        font=('Roboto', 12),
        bg="red",
        fg="white"
        )
    sign_up_username_label.place(x=200, y=150, anchor=W)
    sign_up_username_entry = Entry(sign_up_window)
    sign_up_username_entry.place(x=200, y=175, anchor=W)

    sign_up_password_label = Label(
        sign_up_window,
        text="Create a password (must be atleast 8 characters long) : ",
        font=('Roboto', 12),
        bg="red",
        fg="white"
    )
    sign_up_password_label.place(x=200, y=200, anchor=W)
    sign_up_password_entry = Entry(sign_up_window)
    sign_up_password_entry.place(x=200, y=225, anchor=W)

    sign_up_password_confirm_label = Label(
        sign_up_window,
        text="Confirm your password: ",
        font=('Roboto', 12),
        bg="red",
        fg="white"
    )
    sign_up_password_confirm_label.place(x=200, y=250, anchor=W)
    sign_up_password_confirm_entry = Entry(sign_up_window)
    sign_up_password_confirm_entry.place(x=200, y=275, anchor=W)

    sign_up_button = customtkinter.CTkButton(
        sign_up_window,
        text="Sign Up",
        command=signUp
    )
    sign_up_button.place(x=200, y=350, anchor=W)

    error_label = Label(
        sign_up_window,
        bg="red",
        fg="red"
    )
    error_label.place(x=200, y=390, anchor=W)

    sign_up_window.mainloop()

# LOGIN WINDOW
def open_login_window(): #subroutine for logging into pokedex account

    def login():
        global username

        username = login_username_entry.get()
        password = login_password_entry.get()

        user_data = pd.read_csv('userData.csv')
        df = pd.DataFrame(user_data)

        pasw = df.loc[df["Username"] == username]["Password"].item()
        key = df.loc[df["Username"] == username]["key"].item()
        password, key = encrypt(password, key)

        if password == pasw:
            close_window(login_window)
        elif password != pasw:
            error_label = Label(
                login_window,
                text="Password incorrect, please try again",
                bg="white",
                fg="red"
            )
            error_label.place(x=250, y=260, anchor=W)


    login_window = Tk()
    login_window.geometry("500x500")
    login_window["bg"] = "red"

    back_to_menu = customtkinter.CTkButton(
    login_window,
    text="Back to menu",
    command=lambda: to_prev_window(login_window, intial_window)
    )
    back_to_menu.place(x=30,y=30)

    login_username_label = Label(
        login_window,
        text="Enter username: ",
        font=('Roboto', 12),
        bg="red",
        fg="white"
    )
    login_username_label.place(x=200, y=150, anchor=W)
    login_username_entry = Entry(login_window)
    login_username_entry.place(x=200, y=175, anchor=W)

    login_password_label = Label(
        login_window,
        text="Enter password: ",
        font=('Roboto', 12),
        bg="red",
        fg="white"
    )
    login_password_label.place(x=200, y=200, anchor=W)
    login_password_entry = Entry(login_window)
    login_password_entry.place(x=200, y=225, anchor=W)

    login_button = customtkinter.CTkButton(
        login_window,
        text="Log in",
        command=login
    )
    login_button.place(x=200, y=300, anchor=W)

    login_window.mainloop()

# FORGOT PASSWORD - ! NOT IN USE !
# def open_forgot_password_window(): #subroutine for password recovery

#     def forgot_password(): # if username and account id match then return password
        # username = forgot_pw_username_entry.get()
#         account_id = forgot_pw_account_id_entry.get()

#         user_data = pd.read_csv('userData.csv')
#         df = pd.DataFrame(user_data)

#         acc_id = df.loc[df["Username"] == username]["userID"].item()
#         print(acc_id)

#         if account_id == acc_id:
#             close_window(forgot_pw_window)
#         elif username not in df:
#             error_label.config(
#                 text=f"Account with username '{username}' does not exist",
#                 bg="white",
#                 fg="red"
#             )
#         elif account_id != acc_id:
#             error_label.config(
#                 text="Incorrect account ID, please try again",
#                 bg="white",
#                 fg="red"
#             )


#     forgot_pw_window = Tk()
#     width = forgot_pw_window.winfo_screenwidth()
#     height = forgot_pw_window.winfo_screenheight()
#     forgot_pw_window.geometry("%dx%d" % (width, height))
#     forgot_pw_window["bg"] = "red"
    
    # back_to_menu = customtkinter.CTkButton(
    # sign_up_window,
    # text="Back to menu",
    # command=lambda: to_prev_window(sign_up_window, intial_window)
    # )
    # back_to_menu.place(x=30,y=30)

#     forgot_pw_username_label = Label(
#         forgot_pw_window,
#         text="Enter Username",
#         font=('Roboto', 12),
#         bg="red",
#         fg="white"
#     )
#     forgot_pw_username_label.place(x=(width/2-width/10), y=150, anchor=W)
#     forgot_pw_username_entry = Entry(forgot_pw_window)
#     forgot_pw_username_entry.place(x=(width/2-width/10), y=175, anchor=W)

#     forgot_pw_account_id_label = Label(
#         forgot_pw_window,
#         text="Enter Account ID",
#         font=('Roboto', 12),
#         bg="red",
#         fg="white"
#     )
#     forgot_pw_account_id_label.place(x=(width/2-width/10), y=225, anchor=W)
#     forgot_pw_account_id_entry = Entry(forgot_pw_window)
#     forgot_pw_account_id_entry.place(x=(width/2-width/10), y=250, anchor=W)

#     error_label = Label(
#         forgot_pw_window,
#         bg="red",
#         fg="red"
#     )
#     error_label.place(x=(width/2-width/10), y=295, anchor=W)

#     forgot_pw_button = customtkinter.CTkButton(
#         forgot_pw_window,
#         text="Recover Password",
#         command=forgot_password
#     )
#     forgot_pw_button.place(x=(width/2-width/10), y=340, anchor=W)

    # forgot_pw_window.mainloop()
    pass

# SEARCH POKEDEX FOR POKEMON
def open_main_window(): #subroutine which allows a user to enter a pokemon and receive data about it

    user_data = pd.read_csv('userData.csv')
    user_data_df = pd.DataFrame(user_data)
    party = pd.read_csv('party.csv')
    party_df = pd.DataFrame(party)
    ACCOUNT_ID = user_data_df.loc[user_data_df["Username"] == username]["userID"].item()

    def party_add(pokemon): #subroutine to add pokemon to user's party

        pokemon1 = party_df.loc[party_df["Username"] == username]["Pokemon1"]
        pokemon2 = party_df.loc[party_df["Username"] == username]["Pokemon2"]
        pokemon3 = party_df.loc[party_df["Username"] == username]["Pokemon3"]
        pokemon4 = party_df.loc[party_df["Username"] == username]["Pokemon4"]
        pokemon5 = party_df.loc[party_df["Username"] == username]["Pokemon5"]
        pokemon6 = party_df.loc[party_df["Username"] == username]["Pokemon6"]

        print(pd.isnull(party_df.loc[pokemon1]))

        # pokemon_lst = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
        # for pokemons in pokemon_lst:
        #     if pokemons.isnull():
        #         pokemons = pokemon
        #     else:
        #         print("aaa")

        user_party = {
            "Username": [username],
            "userID": [ACCOUNT_ID],
            "Pokemon1": [pokemon1],
            "Pokemon2": [pokemon2],
            "Pokemon3": [pokemon3],
            "Pokemon4": [pokemon4],
            "Pokemon5": [pokemon5],
            "Pokemon6": [pokemon6]
        }
        user_party = pd.DataFrame(user_party)
        print(user_party)
        user_party.to_csv("party.csv", header=False, index=False, mode="a")

    def search():

        search_result_entry = search_entry.get()

        url = f"https://pokeapi.co/api/v2/pokemon/{search_result_entry.lower()}"
        response = requests.get(url)
        pokemon_data = response.json()

        if response.status_code == 200: # code source - https://medium.com/@mohamed.mywork/learn-apis-with-pok%C3%A9mon-and-python-7003b35b5ba#:~:text=To%20start%20using%20APIs%20with,is%20used%20by%20many%20developers.&text=The%20function%20get_pokemon_info%20first%20takes%20a%20pokemon%20name%20as%20input.
            pokemon_info = {
                "name": pokemon_data["name"],
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
                "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
            }
        else:   # status code 200 is success, the rest are errors
            print("Error, status code:", response.status_code)
            exit()

        pokemon_name = str(pokemon_info["name"]).capitalize() # capitalises the first letter as it is lowercase by default
        pokemon_height = pokemon_info["height"]
        pokemon_weight = pokemon_info["weight"]
        pokemon_abilities = str(pokemon_info["abilities"]).replace("[","")
        pokemon_abilities = pokemon_abilities.replace("]","") # removes the []' characters
        pokemon_abilities = pokemon_abilities.replace("'","")
        pokemon_types = str(pokemon_info["types"]).replace("[","")
        pokemon_types = pokemon_types.replace("]","")
        pokemon_types = pokemon_types.replace("'","")

        search_result_window = Tk()
        search_result_window.geometry("500x500")
        # search_result_window["bg"] = PhotoImage(file="Pokedex\main-bg.png")

        search_result_frame = Frame(search_result_window)
        search_result_frame.place(x=250, y=250, anchor=CENTER)

        # pokemon_image = 

        pokemon_name_label = Label(
            search_result_frame,
            text=pokemon_name,
            font=('Roboto', 12)
        )
        pokemon_name_label.pack(side=TOP)
        pokemon_height_label = Label(
            search_result_frame,
            text=f"Height: {pokemon_height}",
            font=('Roboto', 12)
        )
        pokemon_height_label.pack(side=TOP)
        pokemon_weight_label = Label(
            search_result_frame,
            text=f"Weight: {pokemon_weight}",
            font=('Roboto', 12)
        )
        pokemon_weight_label.pack(side=TOP)
        pokemon_abilities_label = Label(
            search_result_frame,
            text=f"Abilities: {pokemon_abilities}",
            font=('Roboto', 12)
        )
        pokemon_abilities_label.pack(side=TOP)
        pokemon_types_label = Label(
            search_result_frame,
            text=f"Types: {pokemon_types}",
            font=('Roboto', 12)
        )
        pokemon_types_label.pack(side=TOP)

        add_to_party = customtkinter.CTkButton(
            search_result_frame,
            text="Add to my party",
            command=lambda: party_add(pokemon_name)
        )
        add_to_party.pack(side=TOP)

        close_window_button = customtkinter.CTkButton(
            search_result_window,
            text="Back",
            command=lambda: close_window(search_result_window)
        )
        close_window_button.place(x=20,y=15)


        search_result_window.mainloop()


    main_window = Tk()
    width = main_window.winfo_screenwidth()
    height = main_window.winfo_screenwidth()
    main_window.geometry("%dx%d" % (width, height))
    main_window["bg"] = "red"

    back_to_menu = customtkinter.CTkButton(
        main_window,
        text="Back to menu",
        command=lambda: to_prev_window(main_window, intial_window)
    )
    back_to_menu.place(x=30,y=30)

    search_label = Label(
        main_window,
        text="Search Pokemon by Name or ID",
        font=('Roboto', 20)
    )
    search_label.place(x=(width/2), y=300, anchor=CENTER)

    search_frame = Frame(
        main_window,
        bg="red"
    )
    search_frame.place(x=(width/2), y=350, anchor=CENTER)

    search_entry = Entry(
        search_frame,
        font=('Roboto', 15)
    )
    search_entry.pack(side=LEFT)

    search_button = customtkinter.CTkButton(
        search_frame,
        text="Search",
        command=search
    )
    search_button.pack(side=RIGHT)


    main_window.mainloop()

# MAIN LOOP
# intial_window()
# open_main_window()


party = pd.read_csv('party.csv')
party_df = pd.DataFrame(party)
print(party_df)

username = "dylan1"
ACCOUNT_ID = "4442aethee6hh4h"

if username not in party_df:
    user_party = {
        "Username": [username],
        "userID": [ACCOUNT_ID],
    }
    party_df = pd.DataFrame(user_party)
    party_df.to_csv("party.csv", header=False, index=False, mode="a")
    print(party_df)

    if party_df.loc[party_df["Username"] == username]["Pokemon1"].isnull():
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    pokemon2 = party_df.loc[party_df["Username"] == username]["Pokemon2"]
    pokemon3 = party_df.loc[party_df["Username"] == username]["Pokemon3"]
    pokemon4 = party_df.loc[party_df["Username"] == username]["Pokemon4"]
    pokemon5 = party_df.loc[party_df["Username"] == username]["Pokemon5"]
    pokemon6 = party_df.loc[party_df["Username"] == username]["Pokemon6"]

    if pokemon1.isnull():
        print("aa")


print(pd.isnull(party_df.loc[pokemon1]))