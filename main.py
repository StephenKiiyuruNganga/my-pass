import json
from ntpath import join
import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, tkinter.END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    no_of_letters = random.randint(8, 10)
    no_of_symbols = random.randint(2, 4)
    no_of_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for round in range(no_of_letters)]
    random_symbols = [random.choice(symbols) for round in range(no_of_symbols)]
    random_numbers = [random.choice(numbers) for round in range(no_of_numbers)]

    password_list = random_letters + random_symbols + random_numbers

    random.shuffle(password_list)

    new_password = "".join(password_list)

    password_input.insert(0, new_password)

    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_input.get().strip(" ").lower()
    email = email_input.get().strip(" ")
    password = password_input.get().strip(" ")
    website_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops",
                               message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            try:
                # read existing data
                with open("data.json", "r") as file:
                    content = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump(website_dict, file, indent=2)
            else:
                # update existing data
                content.update(website_dict)
                # save updated data
                with open(file="data.json", mode="w") as file:
                    json.dump(content, file, indent=2)
            finally:
                # clear inputs
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data File is empty")
    else:
        website = website_input.get().strip(" ").lower()
        if website in content:
            email = content[f"{website}"]["email"]
            password = content[f"{website}"]["password"]
            messagebox.showinfo(
                title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(
                title="Sorry", message=f"No details for {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200, highlightthickness=0)
logo = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# inputs
website_input = tkinter.Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = tkinter.Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "yourmail@gmail.com")
password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

# buttons
generate_btn = tkinter.Button(text="Generate Password",
                              command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = tkinter.Button(text="Add", width=35, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search",  width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
