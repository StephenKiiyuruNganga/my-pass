import tkinter
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get().strip(" ")
    email = email_input.get().strip(" ")
    password = password_input.get().strip(" ")

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops",
                               message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            with open(file="./data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)


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
website_input = tkinter.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "yourmail@gmail.com")
password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

# buttons
generate_btn = tkinter.Button(text="Generate Password", command=None)
generate_btn.grid(row=3, column=2)
add_btn = tkinter.Button(text="Add", width=30, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
