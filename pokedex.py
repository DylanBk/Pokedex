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
        :key (str): A key which can be used to compare enc_pw with user inputs.
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
    init_window.title=("Menu")
    # init_window["bg"] = PhotoImage(file = "main-bg.png")

    welcome_label = Label(
        init_window,
        text="-  Welcome to the Pokédex  -",
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

    init_window.mainloop()


# SIGN UP WINDOW
def open_sign_up_window(): #subroutine for signing up for a pokedex account

     # SET UP ACCOUNT
    def signUp():
        global username

        username = sign_up_username_entry.get()
        password = sign_up_password_entry.get()
        password_confirm = sign_up_password_confirm_entry.get()

        user_data = pd.read_csv('UserData.csv')
        user_data_df = pd.DataFrame(user_data)

        user_list = user_data_df.Username.to_list()

        if len(user_list) >= 5:
            error_label.config(
                text="Maximum of six users has already been reached",
                bg="white",
                fg="red"
            )
        elif username == "":
            error_label.config(
                text="Username cannot be blank",
                bg="white",
                fg="red"
            )
        elif username in user_list:
            error_label.config(
                text=f"An account with the username '{username}' already exists",
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

            sequence_samples = ["9E3DtL51lOddK9qJCGZL", "1ZyaBqDskPGMwWaS5Ktf", "z8QVNnwQfsjrLJepbuta", "aAX4ka6vtZ3xHtMjnDKN", "3wqJdVFny4NLn7TTOHOo", "Whowy3ZGT1ne1Ol92MDV", "1mSQmTMYaShg32oH9vaF", "8RcamxL4ompFC3cvcOQX", "GfAVgHcq4x9uMwPbSJ7u", "jqXBfzGK8imwbIxSb2gx"]
            sequence_unmixed = random.choice(sequence_samples)
            sequence_mixed = ''.join(random.choices(sequence_unmixed, k=15))
            ACCOUNT_ID = sequence_mixed
           
            user_data = {
                "Username": [username],
                "Password": [enc_pw],
                "userID": [ACCOUNT_ID],
                "key": [key],
                "DisplayName": [username],
                "Pokemon1": 0,
                "Pokemon2": 0,
                "Pokemon3": 0,
                "Pokemon4": 0,
                "Pokemon5": 0,
                "Pokemon6": 0
            }
            user_data_df = pd.DataFrame(user_data)
            user_data_df.to_csv("UserData.csv", header=False, index=False, mode='a')

            sign_up_window.destroy()
            open_main_window()

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

        error_label = Label(
            login_window,
            text="",
            bg="white"
        )
        error_label.place(x=250, y=260, anchor=CENTER)

        username = login_username_entry.get()
        password = login_password_entry.get()

        user_data = pd.read_csv('UserData.csv')
        df = pd.DataFrame(user_data)

        user_list = df["Username"].to_list()

        count = 0
        if len(user_list) < 1:
            error_label.config(
                text=f"An account with the username '{username}' does not exist",
                bg ="white",
                fg="red"
            )
        else:
            for i in user_list:
                count += 1
                if count > len(user_list)-1: # -1 to account for list indexing starting at 0
                    error_label.config(
                        text=f"An account with the username '{username}' does not exist",
                        bg ="white",
                        fg="red"
                    )

                if username == i:
                    error_label.config(
                        text="",
                        bg="red"
                  )

                pasw = df.loc[df["Username"] == username]["Password"].item()
                key = df.loc[df["Username"] == username]["key"].item()
                password, key = encrypt(password, key)

                if password == pasw:
                    login_window.destroy()
                    open_main_window()
                elif password != pasw:
                    error_label.config(
                        text="Password incorrect, please try again",
                        bg="white",
                        fg="red"
                    )



        if username == i:
            pasw = df.loc[df["Username"] == username]["Password"].item()
            key = df.loc[df["Username"] == username]["key"].item()
            password, key = encrypt(password, key)

            if password == pasw:
                login_window.destroy()
                open_main_window()
            elif password != pasw:
                error_label.config(
                    text="Password incorrect, please try again",
                    bg="white",
                    fg="red"
                )


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


# SEARCH POKEDEX FOR POKEMON
def open_main_window(): # opens main window

    user_data = pd.read_csv('UserData.csv')
    user_data_df = pd.DataFrame(user_data)

    i = user_data_df.index[user_data_df.Username == username].tolist() # get index of user in use
    i = i[0] # list to string

        # ADD TO PARTY
    def party_add(pokemon_name, window): #subroutine to add pokemon to user's party
        """
        ...Adds a chosen pokemon to the user's party.

        Args:
            :param pokemon_name (str): The Pokemon to be added to the user's party.
            :param window (var): The tkinter window in use.
        """        

        pk1 = user_data_df.loc[i, ["Pokemon1"]].to_string().replace("Pokemon1", "").strip() # convert value in df to a string without the column name
        pk2 = user_data_df.loc[i, ["Pokemon2"]].to_string().replace("Pokemon2", "").strip()
        pk3 = user_data_df.loc[i, ["Pokemon3"]].to_string().replace("Pokemon3", "").strip()
        pk4 = user_data_df.loc[i, ["Pokemon4"]].to_string().replace("Pokemon4", "").strip()
        pk5 = user_data_df.loc[i, ["Pokemon5"]].to_string().replace("Pokemon5", "").strip()
        pk6 = user_data_df.loc[i, ["Pokemon6"]].to_string().replace("Pokemon6", "").strip()

        error_label = Label(
            window,
            text="",
            font=('Roboto', 12),
            bg="white",
            fg="white",
        )
        error_label.place(x=250, y=400, anchor=CENTER)
        error_label.destroy()

        if pk1 == pokemon_name: # if any of these are '0', it's because that pokemon cell is empty and can be added to
            error_label = Label( # if it's NOT '0', it's because there is a pokemon currently in that cell
                window,
                text=f"You already have {pokemon_name} on your team!",
                bg="white",
                fg="red"
            )
            error_label.place(x=250, y=400, anchor=CENTER)
        elif pk1 == "0":
            user_data_df.loc[i, "Pokemon1"] = pokemon_name
            user_data_df.to_csv('UserData.csv', index=False)
        else:
            if pk2 == pokemon_name:
                error_label = Label(
                    window,
                    text=f"You already have {pokemon_name} on your team!",
                    bg="white",
                    fg="red"
                )
                error_label.place(x=250, y=400, anchor=CENTER)            
            elif pk2 == "0":
                user_data_df.loc[i, "Pokemon2"] = pokemon_name
                user_data_df.to_csv('UserData.csv', index=False)
            else:
                if pk3 == pokemon_name:
                    error_label = Label(
                        window,
                        text=f"You already have {pokemon_name} on your team!",
                        bg="white",
                        fg="red"
                    )
                    error_label.place(x=250, y=400, anchor=CENTER)
                elif pk3 == "0":
                    user_data_df.loc[i, "Pokemon3"] = pokemon_name
                    user_data_df.to_csv('UserData.csv', index=False)
                else:
                    if pk4 == pokemon_name:
                        error_label = Label(
                            window,
                            text=f"You already have {pokemon_name} on your team!",
                            bg="white",
                            fg="red"
                        )
                        error_label.place(x=250, y=400, anchor=CENTER)
                    elif pk4 == "0":
                        user_data_df.loc[i, "Pokemon4"] = pokemon_name
                        user_data_df.to_csv('UserData.csv', index=False)
                    else:
                        if pk5 == pokemon_name:
                            error_label = Label(
                                window,
                                text=f"You already have {pokemon_name} on your team!",
                                bg="white",
                                fg="red"
                            )
                            error_label.place(x=250, y=400, anchor=CENTER)
                        elif pk5 == "0":
                            user_data_df[i, "Pokemon5"] = pokemon_name
                            user_data_df.to_csv('UserData.csv', index=False)
                        else:
                            if pk6 == pokemon_name:
                                error_label = Label(
                                    window,
                                    text=f"You already have {pokemon_name} on your team!",
                                    bg="white",
                                    fg="red"
                                )
                                error_label.place(x=250, y=400, anchor=CENTER)
                            elif pokemon_name == "0":
                                user_data_df[i, "Pokemon6"] = pokemon_name
                                user_data_df.to_csv('UserData.csv', index=False)
                            else:
                                error_label = Label(
                                    window,
                                    text=f"You already have 6 Pokémon on your team!",
                                    bg="white",
                                    fg="red"
                                )
                                error_label.place(x=250, y=400, anchor=CENTER)


    def party_replace(): # subroutine to replace a pokemon from user's party
        pass


    def view_party(): # subroutine to view all (if any) pokemon in user's party
        """
        ...Displays all Pokemon in the user's party.
        """

        def party_remove(): # subroutine to remove a pokemon from user's party
            def remove_pokemon(pokemon):
                """
                ...Removes a chosen Pokemon from the user's party.

                Args:
                    :param pokemon (var): The Pokemon as a tkinter entry to be removed from the party. 
                """

                error_label = Label(
                    main_window,
                    text="",
                    bg="red"
                )
                error_label.place(x=(width/2), y=700, anchor=CENTER)
                error_label.destroy()

                pokemon_name = pokemon.get()
                pokemon_name = pokemon_name.capitalize() # capitalize makes sure that first char is upper and the rest are lower to prevent errors caused by inputs such as 'piKAcHu'
                options = ["Pokemon1", "Pokemon2", "Pokemon3", "Pokemon4", "Pokemon5", "Pokemon6"]

                count = 0
                for j in options:
                    count += 1
                    print(count)
                    x = user_data_df.loc[i, j]
                    if x == pokemon_name:
                        user_data_df.loc[i, j] = 0
                        user_data_df.to_csv('UserData.csv', index=False)
                        party_remove_frame.destroy()
                        view_party_frame.destroy()
                    elif count == 6 and x != pokemon_name: # display error message once compared with all 6 and no matches
                        error_label = Label(
                            text=f"{pokemon_name} is not in your party",
                            bg="white",
                            fg="red"
                        )
                        error_label.place(x=(width/2), y=700, anchor=CENTER)


            party_remove_frame = Frame(
                view_party_frame,
                bg="white"
            )
            party_remove_frame.pack(padx=5, pady=5, side=RIGHT)
            party_remove_entry = Entry(
                party_remove_frame,
                font=('Roboto', 12)
            )
            party_remove_entry.pack(side=LEFT)
            party_remove_button = customtkinter.CTkButton(
                party_remove_frame,
                text="Confirm",
                command=lambda: remove_pokemon(party_remove_entry)
            )
            party_remove_button.pack(side=RIGHT)


        pk1 = user_data_df.loc[i, ["Pokemon1"]].to_string().replace("Pokemon1", "").strip() # convert value in df to a string without the column name
        pk2 = user_data_df.loc[i, ["Pokemon2"]].to_string().replace("Pokemon2", "").strip()
        pk3 = user_data_df.loc[i, ["Pokemon3"]].to_string().replace("Pokemon3", "").strip()
        pk4 = user_data_df.loc[i, ["Pokemon4"]].to_string().replace("Pokemon4", "").strip()
        pk5 = user_data_df.loc[i, ["Pokemon5"]].to_string().replace("Pokemon5", "").strip()
        pk6 = user_data_df.loc[i, ["Pokemon6"]].to_string().replace("Pokemon6", "").strip()

        view_party_frame = Frame(
            main_window,
            bg="azure3"
        )
        view_party_frame.place(x=(width/2), y=550, anchor=CENTER)

        if pk1 == 0 and pk2 == 0 and pk3 == 0 and pk4 == 0 and pk5 == 0 and pk6 == 0:
            error_label = Label(
                view_party_frame,
                text="You currently have no Pokémon in your party",
                font=('Roboto', 12),
                fg="red"
            )
            error_label.pack()
        else:
            error_label.destroy()
            if pk1 == 0:
                pk1 = "N/A"
            if pk2 == 0:
                pk2 = "N/A"
            if pk3 == 0:
                pk3 = "N/A"+
            if pk4 == 0:
                pk4 = "N/A"
            if pk5 == 0:
                pk5 = "N/A"
            if pk6 == 0:
                pk6 = "N/A"
            party = (f"Your party consists of: \n- {pk1}\n- {pk2}\n- {pk3}\n- {pk4}\n- {pk5}\n- {pk6}")
            party_label = Label(
                view_party_frame,
                text=party,
                font=('Roboto', 12),
                bg="cyan3",
                fg="white"
            )
            party_label.pack(side=TOP)

            remove_party_button = customtkinter.CTkButton(
                view_party_frame,
                text="Remove a Pokémon",
                command=party_remove
            )
            remove_party_button.pack(pady=10, side=BOTTOM)
        
        hide_party_button = customtkinter.CTkButton(
            view_party_frame,
            text="Hide Party",
            command=lambda: view_party_frame.destroy()#, error_label.destroy() 
        )
        hide_party_button.pack(pady=10, side=BOTTOM)


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

        url = f"https://pokeapi.co/api/v2/pokemon/{search_result_entry.lower()}" # pass user input into the API URL
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
        pokemon_abilities = pokemon_abilities.replace("]","") # removes extra/redundant characters
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
            command=lambda: party_add(pokemon_name, search_result_window)
        )
        add_to_party.pack(side=TOP)

        close_window_button = customtkinter.CTkButton(
            search_result_window,
            text="Back",
            command=lambda: close_window(search_result_window)
        )
        close_window_button.place(x=20,y=15)


        search_result_window.mainloop()


    def search_by_type():
        pass


    def open_settings(): #subroutine for user to access and change account settings
        def confirm(entry, choice, frame): # confirm changed username/password/display name
            """
            ...Used to confirm username/password change.

            Args:
                :param entry (var): The name of the tkinter entry to get the input from.
                :param choice (str): The name of the column to edit.
                :param frame (var): The name of the tkinter frame to be destroyed.
            """

            error_label = Label(
                settings_window,
                text="",
                bg="thistle3",
                fg="red"
            )
            error_label.place(x=250, y=430, anchor=CENTER)

            x = entry.get()

            if choice == "Username":
                user_list= user_data_df.Username.to_list()
                if x == "":
                    error_label.config(
                        text="Username cannot be blank",
                        bg="white"
                    )
                elif x in user_list:
                    error_label.config(
                        text=f"An account with the username '{x}' already exists",
                        bg="white"
                        )
                else:
                    user_data_df.loc[i, choice] = x
                    user_data_df.to_csv('UserData.csv', index=False)
                    frame.destroy()
                    error_label.destroy()
            elif choice == "DisplayName":
                    if x == "":
                        user_data_df.loc[i, choice] = username
                        user_data_df.to_csv('UserData.csv', index=False)
                        frame.destroy()
                        error_label.destroy()
                    else:
                        user_data_df.loc[i, choice] = x
                        user_data_df.to_csv('UserData.csv', index=False)
                        frame.destroy()
                        error_label.destroy()
            elif choice == "Password":
                if len(x) < 8:
                    error_label.config(
                        text="Password must be longer than 8 characters",
                        bg="white"
                    )
                else:
                    enc_pw, key = encrypt(x, None)
                    user_data_df.loc[i, choice] = enc_pw
                    user_data_df.loc[i, "key"] = key
                    user_data_df.to_csv('UserData.csv', index=False)
                    frame.destroy()
                    error_label.destroy()


        def change_username(): # subroutine to change username
            new_username_frame = Frame(
                settings_window,
                bg="thistle3"
                )
            new_username_frame.place(x=250, y=180, anchor=CENTER)
            new_username_label = Label(
                new_username_frame,
                text="Enter new username:",
                font=('Roboto', 12),
                bg="thistle3"
            )
            new_username_label.pack(side=LEFT)
            new_username_entry = Entry(
                new_username_frame,
                font=('Roboto', 12),
                bg="white"
            )
            new_username_entry.pack(side=LEFT)
            new_username_button = customtkinter.CTkButton(
                new_username_frame,
                text="Confirm",
                command=lambda: confirm(new_username_entry, "Username", new_username_frame)
            )
            new_username_button.pack(side=RIGHT)


        def change_display_name():
            new_display_name_frame = Frame(
                settings_window,
                bg="thistle3"
                )
            new_display_name_frame.place(x=250, y=250, anchor=CENTER)
            new_display_name_label = Label(
                new_display_name_frame,
                text="Enter new display name:",
                font=('Roboto', 12),
                bg="thistle3"
            )
            new_display_name_label.pack(side=LEFT)
            new_display_name_entry = Entry(
                new_display_name_frame,
                font=('Roboto', 12),
                bg="white"
            )
            new_display_name_entry.pack(side=LEFT)
            new_display_name_button = customtkinter.CTkButton(
                new_display_name_frame,
                text="Confirm",
                command=lambda: confirm(new_display_name_entry, "DisplayName", new_display_name_frame)
            )
            new_display_name_button.pack(side=RIGHT)


        def change_password(): # subroutine to change password
            new_password_frame = Frame(
                settings_window,
                bg="thistle3"
                )
            new_password_frame.place(x=250, y=320, anchor=CENTER)
            new_password_label = Label(
                new_password_frame,
                text="Enter new password:",
                font=('Roboto', 12),
                bg="thistle3"
            )
            new_password_label.pack(side=LEFT)
            new_password_entry = Entry(
                new_password_frame,
                font=('Roboto', 12),
                bg="white"
            )
            new_password_entry.pack(side=LEFT)
            new_password_button = customtkinter.CTkButton(
                new_password_frame,
                text="Confirm",
                command=lambda: confirm(new_password_entry, "Password", new_password_frame)
            )
            new_password_button.pack(side=RIGHT)


        def view_id():
            Id = user_data_df.loc[i, ["userID"]].to_string().replace("userID", "").strip()
            id_frame = Frame(
                settings_window,
                bg="thistle3"
            )
            id_frame.place(x=250, y=390, anchor=CENTER)
            id_label = Label(
                id_frame,
                text=f"Your account ID is {Id}",
                font=('Roboto', 11),
                bg="thistle3"
            )
            id_label.pack(side=LEFT)
            hide_id_button = customtkinter.CTkButton(
                id_frame,
                text="Hide ID",
                command=id_frame.destroy
            )
            hide_id_button.pack(side=RIGHT)



        settings_window = Tk()
        settings_window.geometry("500x500")
        settings_window["bg"] = "thistle3"

        back_button = customtkinter.CTkButton(
            settings_window,
            text="Close",
            command=lambda: close_window(settings_window)
        )
        back_button.place(x=30, y=30, anchor=W)

        settings_label = Label(
            settings_window,
            text="Settings",
            font=('Roboto', 20),
            bg="thistle3"
        )
        settings_label.place(x=250, y=50, anchor=CENTER)

        change_username_button = customtkinter.CTkButton(
            settings_window,
            text="Change Username",
            command=change_username
        )
        change_username_button.place(x=250, y=150, anchor=CENTER)

        change_display_name_button = customtkinter.CTkButton(
            settings_window,
            text="Change Display Name",
            command=change_display_name
        )
        change_display_name_button.place(x=250, y=220, anchor=CENTER)

        change_password_button = customtkinter.CTkButton(
            settings_window,
            text="Change Password",
            command=change_password
        )
        change_password_button.place(x=250, y=290, anchor=CENTER)

        view_id_button = customtkinter.CTkButton(
            settings_window,
            text="View Account ID",
            command=view_id
        )
        view_id_button.place(x=250, y=360, anchor=CENTER)


        settings_window.mainloop()


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
    back_to_menu.place(x=30,y=30, anchor=W)

    settings_button = customtkinter.CTkButton(
        main_window,
        text="Settings",
        command=open_settings
    )
    settings_button.place(x=(width-30) ,y=30, anchor=E)

    search_label = Label(
        main_window,
        text="Search Pokémon by Name or ID",
        font=('Roboto', 25),
        bg="red",
        fg="white"
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

    view_party_button = customtkinter.CTkButton(
        main_window,
        text="View party",
        command=view_party
    )
    view_party_button.place(x=(width/2), y=400, anchor=CENTER)


    main_window.mainloop()

# MAIN LOOP
intial_window()