from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

DEFAULT_USERNAME = "example@xxxx.com"


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    web = web_input.get()
    try:
        with open("safeguard.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message=f"No password file found.")
    else:
        if web in data:
            username = data[web]["username"]
            password = data[web]["password"]
            messagebox.showinfo(message=f"Website: {web}"
                                        f"\n Username: {username}"
                                        f"\n Password: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(message=f"No password found for {web}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    # clear the input
    password_input.delete(0, END)

    # generate the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    # output the password generated
    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # get the inputs
    web = web_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        web: {
            "username": username,
            "password":password,
        }
    }

    # check if any blank
    if len(web) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(message="Please fill in all the blanks.")

    else:
        # info check
        is_ok = messagebox.askokcancel(message=f"There are the details entered: "
                                               f"\nWebsite: {web}"
                                               f"\nEmail: {username}"
                                               f"\nPassword: {password}"
                                               f"\nIs it okay to save?")
        # save the info
        if is_ok:
            try:
                with open("safeguard.json", mode="r") as file:
                    # read the old data
                    data = json.load(file)
            except FileNotFoundError:
                data = new_data
            else:
                # update the old data with the new data
                data.update(new_data)

            with open("safeguard.json", mode="w") as file:
                # save updated data
                json.dump(data, file, indent=4)

            # clear the inputs
            web_input.delete(0, END)
            password_input.delete(0, END)
            # reset the cursor
            web_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

# set a window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# set the canvas of the logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

# set the website part
web_label = Label(text="Website:")
web_label.grid(column=1, row=2)

web_input = Entry()
web_input.focus()
web_input.grid(column=2, row=2, sticky="W")

search_button = Button(text="Search", padx=5, command=search)
search_button.grid(column=3, row=2, sticky="EW")

# set the email/username part
username_label = Label(text="Email/Username:")
username_label.grid(column=1, row=3)

username_input = Entry()
username_input.grid(column=2, row=3, columnspan=2, sticky="EW")
username_input.insert(0, DEFAULT_USERNAME)

# set the password part
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

password_input = Entry()
password_input.grid(column=2, row=4, sticky="W")

password_button = Button(text="Generate Password", padx=5, command=password_generator)
password_button.grid(column=3, row=4)

# set add button
add_button = Button(text="Add", command=save_password)
add_button.grid(column=2, row=5, columnspan=2, sticky="EW")

# keep the window
window.mainloop()
