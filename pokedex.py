# IMPORTS
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import pandas as pd
import requests
import urllib.request
from io import BytesIO
import random

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


# CLOSE WINDOWS
def close_window(window): #destroys the window from which it is called from
    """

    ...Closes the window which is passed as an argument.
    
    Args:
        :param window (var): The window to be closed
    """
    window.destroy()

# TO LAST WINDOW
def to_prev_window(current, previous):#destroys current window and opens the previous window
    """
    ...Closes the current window and opens the previous window.
    
    Args:
    :param current (var): The window currently open.
    :param previous (func): The function which opens the previous window.
    """
    current.destroy()
    previous()

# ENCRYPT PW
def encrypt(password, key): #encrypts passwords, creates a key used to compare entered pw and stored pw
    """
    ...Encrypts a unicode input and returns the encrypted password as well as the key.

    Args:
        :param password (str): The string to be encrypted.
        :param key (int): If available, the key used to manipulate the encrpytion.

    Returns:
        :enc_pw (str): The encrypted string.
        :key(str): A key which can be used to compare enc_pw with user inputs.
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
            df.to_csv("userData.csv", header=False, index=False, mode='a')

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
def open_main_window(): # opens main window

    user_data = pd.read_csv('userData.csv')
    user_data_df = pd.DataFrame(user_data)
    party = pd.read_csv('party.csv')
    party_df = pd.DataFrame(party)
    ACCOUNT_ID = user_data_df.loc[user_data_df["Username"] == username]["userID"].item()

        # ADD TO PARTY
    def party_add(pokemon_name): #subroutine to add pokemon to user's party !!!NEED TO MAKE IT SO NEW TEAM OVERWRITES OLD TEAM WITHOUT OVERWRITING WHOLE FILE!!!
        """
        ...Adds a chosen pokemon to the user's party.

        Args:
            :param pokemon_name(str): The Pokemon to be added to the user's party
        """
        party = pd.read_csv('party.csv')
        party_df = pd.DataFrame(party)

        user_check = (party_df.loc[party_df.Username == username])

        if len(user_check) < 1: # check if their username exists in the CSV file
            new_user = {
                "Username": [username],
                "userID": [ACCOUNT_ID],
                "Pokemon1": 0,
                "Pokemon2": 0,
                "Pokemon3": 0,
                "Pokemon4": 0,
                "Pokemon5": 0,
                "Pokemon6": 0
            }
            new_user_df = pd.DataFrame(new_user) # if their username is not in the party, it adds them to it, the 0s are placeholders
            new_user_df.to_csv('party.csv', header=False, index=False, mode='a')
        
        i = party_df.index[party_df.Username == username].tolist() # get index of user in use
        i = i[0]

        pk1 = party_df.loc[i, ["Pokemon1"]].to_string().replace("Pokemon1", "").strip()
        pk2 = party_df.loc[i, ["Pokemon2"]].to_string().replace("Pokemon2", "").strip()
        pk3 = party_df.loc[i, ["Pokemon3"]].to_string().replace("Pokemon3", "").strip()
        pk4 = party_df.loc[i, ["Pokemon4"]].to_string().replace("Pokemon4", "").strip()
        pk5 = party_df.loc[i, ["Pokemon5"]].to_string().replace("Pokemon5", "").strip()
        pk6 = party_df.loc[i, ["Pokemon6"]].to_string().replace("Pokemon6", "").strip()

        if pk1 == pokemon_name: # if any of these are '0', it's because that pokemon cell is empty and can be added to
            print(f"You already have {pokemon_name} on your team!") # if it's NOT '0', it's because there is a pokemon currently in that cell
        elif pk1 == "0": # a, b, c, d, & e are used as temp vars to ensure previously added pokemon are not overwritten
            new_team = {
                "Username": [username],
                "userID": [ACCOUNT_ID],
                "Pokemon1": [pokemon_name],
                "Pokemon2": 0,
                "Pokemon3": 0,
                "Pokemon4": 0,
                "Pokemon5": 0,
                "Pokemon6": 0
            }
            new_team_df = pd.DataFrame(new_team)
            print(new_team_df)
            
            new_team_df.to_csv('party.csv', header=False, index=False, mode='a')

            print(party_df)

        else:
            if pk2 == pokemon_name:
                print(f"You already have {pokemon_name} on your team!")                    
            elif pk2 == "0":
                a = party_df.loc[i, ["Pokemon1"]]
                a = a.to_string()
                a = a.replace("Pokemon1", "")
                a = a.strip()

                new_team = {
                    "Username": [username],
                    "userID": [ACCOUNT_ID],
                    "Pokemon1": [a],
                    "Pokemon2": [pokemon_name],
                    "Pokemon3": 0,
                    "Pokemon4": 0,
                    "Pokemon5": 0,
                    "Pokemon6": 0
                }
                new_team_df = pd.DataFrame(new_team)
                new_team_df.to_csv('party.csv', header=False, index=False, mode='a')
            else:
                if pk3 == pokemon_name:
                    print(f"You already have {pokemon_name} on your team!")
                elif pk3 == "0":
                    a = party_df.loc[i, ["Pokemon1"]]
                    a = a.to_string()
                    a = a.replace("Pokemon1", "")
                    a = a.strip()
                    b = party_df.loc[i, ["Pokemon2"]]
                    b = b.to_string()
                    b = b.replace("Pokemon2", "")
                    b = b.strip()

                    new_team = {
                    "Username": [username],
                    "userID": [ACCOUNT_ID],
                    "Pokemon1": [a],
                    "Pokemon2": [b],
                    "Pokemon3": [pokemon_name],
                    "Pokemon4": 0,
                    "Pokemon5": 0,
                    "Pokemon6": 0
                    }
                    new_team_df = pd.DataFrame(new_team)
                    new_team_df.to_csv('party.csv', header=False, index=False, mode='a')
                else:
                    if pk4 == pokemon_name:
                        print(f"You already have {pokemon_name} on your team!")
                    elif pk4 == "0":
                        a = party_df.loc[i, ["Pokemon1"]]
                        a = a.to_string()
                        a = a.replace("Pokemon1", "")
                        a = a.strip()
                        b = party_df.loc[i, ["Pokemon2"]]
                        b = b.to_string()
                        b = b.replace("Pokemon2", "")
                        b = b.strip()
                        c = party_df.loc[i, ["Pokemon3"]]
                        c = c.to_string()
                        c = c.replace("Pokemon3", "")
                        c = c.strip()

                        new_team = {
                        "Username": [username],
                        "userID": [ACCOUNT_ID],
                        "Pokemon1": [a],
                        "Pokemon2": [b],
                        "Pokemon3": [c],
                        "Pokemon4": [pokemon_name],
                        "Pokemon5": 0,
                        "Pokemon6": 0
                        }
                        new_team_df = pd.DataFrame(new_team)
                        new_team_df.to_csv('party.csv', header=False, index=False, mode='a')
                    else:
                        if pk5 == pokemon_name:
                            print(f"You already have {pokemon_name} on your team!")
                        elif pk5 == "0":
                            a = party_df.loc[i, ["Pokemon1"]]
                            a = a.to_string()
                            a = a.replace("Pokemon1", "")
                            a = a.strip()
                            b = party_df.loc[i, ["Pokemon2"]]
                            b = b.to_string()
                            b = b.replace("Pokemon2", "")
                            b = b.strip()
                            c = party_df.loc[i, ["Pokemon3"]]
                            c = c.to_string()
                            c = c.replace("Pokemon3", "")
                            c = c.strip()
                            d = party_df.loc[i, ["Pokemon4"]]
                            d = d.to_string()
                            d = d.replace("Pokemon4", "")
                            d = d.strip()

                            new_team = {
                            "Username": [username],
                            "userID": [ACCOUNT_ID],
                            "Pokemon1": [a],
                            "Pokemon2": [b],
                            "Pokemon3": [c],
                            "Pokemon4": [d],
                            "Pokemon5": [pokemon_name],
                            "Pokemon6": 0
                            }
                            new_team_df = pd.DataFrame(new_team)
                            new_team_df.to_csv('party.csv', header=False, index=False, mode='a')
                        else:
                            if pk6 == pokemon_name:
                                print("You already have 6 Pokemon on your team!")
                            elif pokemon_name == "0":
                                a = party_df.loc[i, ["Pokemon1"]]
                                a = a.to_string()
                                a = a.replace("Pokemon1", "")
                                a = a.strip()
                                b = party_df.loc[i, ["Pokemon2"]]
                                b = b.to_string()
                                b = b.replace("Pokemon2", "")
                                b = b.strip()
                                c = party_df.loc[i, ["Pokemon3"]]
                                c = c.to_string()
                                c = c.replace("Pokemon3", "")
                                c = c.strip()
                                d = party_df.loc[i, ["Pokemon4"]]
                                d = d.to_string()
                                d = d.replace("Pokemon4", "")
                                d = d.strip()
                                e = party_df.loc[i, ["Pokemon5"]]
                                e = e.to_string()
                                e = e.replace("Pokemon5", "")
                                e = e.strip()

                                new_team = {
                                "Username": [username],
                                "userID": [ACCOUNT_ID],
                                "Pokemon1": [a],
                                "Pokemon2": [b],
                                "Pokemon3": [c],
                                "Pokemon4": [d],
                                "Pokemon5": [e],
                                "Pokemon6": [pokemon_name]
                                }
                                new_team_df = pd.DataFrame(new_team)
                                new_team_df.to_csv('party.csv', header=False, index=False, mode='a')
                            else:
                                print("error")


    def search():
        """
        ...Allows user to seach any Pokemon by name or by ID,
        data is retrieved from the PokeAPI
        """

        def display_image_from_url(url): # code source - https://www.tutorialspoint.com/displaying-images-from-url-in-tkinter
            """
            ...converts images fetched from a URL to an actual image to be displayed by tkinter

            Args:
                :param url: The url of the image to be retrieved.
            """
            with urllib.request.urlopen(url) as u:
                raw_data = u.read()

            image = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(image)

            pk_image = Tk()

            label = Label(pk_image, image=photo)
            label.pack()

            pk_image.mainloop()


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
                "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
                "sprite_front": pokemon_data["sprites"]["front_default"],
                "sprite_back": pokemon_data["sprites"]["back_default"]
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
        pokemon_sprite_f = pokemon_info["sprite_front"]
        pokemon_sprite_b = pokemon_info["sprite_back"]


        search_result_window = Tk()
        search_result_window.geometry("500x500")
        # search_result_window["bg"] = PhotoImage(file="Pokedex\main-bg.png")

        search_result_frame = Frame(search_result_window)
        search_result_frame.place(x=250, y=250, anchor=CENTER)

        # display_image_from_url(pokemon_sprite_f)

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

        error_label = Label(
            search_result_frame,
            text="",
            font=('Roboto', 12),
            bg="red",
            fg="red"
        )
        error_label.pack(side=TOP)

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
intial_window()
open_main_window()


#PANDAS UTILITIES

# print(party_df["Username"]) #returns usernames
# print(party_df[["Username", "Pokemon1"]]) #returns usernames and items in Pokemon1
# print(party_df[party_df.index==1]) #returns items on index/row 1
# print(party_df[party_df.index.isin(range(1,4))]) #returns items on the indexes between 0 and 4
# print(party_df.loc[1]) #returns a pandas Series of items at the index labelled 1, not set in this csv so it returns items at location 1 by default
# print(party_df.iloc[1]) #returns a pandas Series of items at index location 1
# print(party_df.loc[2:5]) #returns rows between 1 and 5
# print(party_df.loc[[1,2,4]]) #returns items at indexes labelled 1, 2, & 4
# print(party_df.iloc[[1,2,4]]) #returns items at index locations 1, 2, & 4
# print(party_df.loc[2:5, ["Username", "Pokemon2", "Pokemon5"]]) #returns items at indexes between 1 & 5 in the columns passed as args
# print(party_df.iloc[2:5, :2]) #returns items at indexes between 1 and 5 in the first 2 columns
# print(party_df.loc[2:, ["userID", "Pokemon4"]]) #returns items after the first 2 indexes and in the passed columns
# print(party_df.iloc[2:,:3]) #returns items after the first 2 rows and in the first 3 columns
# print(party_df[party_df.Username == "Dylan1"]) #returns items in the same row as the Username 'Dylan1'
# print(party_df.loc[party_df["number"] > 20]) #returns all rows where the column 'number' is greater than 20
# print(party_df.loc[party_df["number"] > 20, ["Username", "Pokemon3"]]) #returns items in the passed columns where the relational column 'number' is greater than 20
# print(party_df.isnull().sum()) #returns sum of null values in each column
# party_df.dropna() #removes all rows with Null values

# party_df2 = pd.concat([party_df,party_df]) #returns a df with duplicates of all rows
# print(party_df2)
# party_df2 = party_df2.drop_duplicates() #removes all duplicates
# print(party_df2)

# party_df2.rename(columns = {"userID":"ID"}, inplace = True) #renames the column from args1 to args2
# print(party_df2) #inplace = True commits the changes to the df
# party_df2.columns = ["col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"] #assigns column names
# print(party_df2)
# print(party_df["number"].mean()) #returns the mean of the 'number' column
# #there is also mode and median

# print("end")