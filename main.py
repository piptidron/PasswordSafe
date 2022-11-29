from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# PASSWORD GENERATOR

def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)




# SAVE PASSWORD

def add_data():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }}

    if website == "" or password == "":
        messagebox.showinfo(message="You leave any fields empty!")
    else:
        try:
            with open ("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open ("data.json", "w") as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)

            with open ("data.json", "w") as file:
                json.dump(data,file,indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)

# SEARCH PASSWORD

def search():
    website = website_input.get()
    try:
        with open ("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found! ")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email:{data[website]['email']}\n"
                                        f"Password:{data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# USER GRAPHICS

window = Tk()
window.title("Password Master")
window.config(padx=20, pady=20)

# PICTURE

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1,row=0)

# INPUTS

website_input = Entry(width=21)
website_input.grid(column=1,row=1)
website_input.focus()
password_input = Entry(width=21)
password_input.grid(column=1,row=3)
email_input = Entry(width=36)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0, "Your Email")

# LABELS

website_label = Label(text="Website:", fg="black", font=("Arial", 14, "bold"))
website_label.grid(column=0,row=1)
email_label = Label(text="Email / Username:", fg="black", font=("Arial",14,"bold"))
email_label.grid(column=0,row=2)
password_label = Label(text="Password:", fg="black", font=("Arial",14,"bold"))
password_label.grid(column=0,row=3)

# BUTTON

gen_password = Button(text="Generate Password", highlightthickness=0,width=11,command=generator)
gen_password.grid(column=2,row=3)
add_button = Button(text="Add", highlightthickness=0,width=34,command=add_data)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search", highlightthickness=0,width=11,command=search)
search_button.grid(column=2,row=1)


window.mainloop()
