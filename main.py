from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_my_password():
    password_entry.delete(0, END)
    password_entry.insert(0, generate_password())
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title='Error', message='Please enter a valid website, email, and password.')
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        except json.JSONDecodeError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
bg_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0, pady=(0, 20))

website_label = Label(text='Website:', bg='white', fg='black')
website_label.grid(column=0, row=1, pady=5)

website_entry = Entry(width=35, bg='white', fg='black', highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=2, pady=5)
website_entry.focus()

email_label = Label(text='Email/Username:', bg='white', fg='black')
email_label.grid(column=0, row=2, pady=5)

email_entry = Entry(width=35, bg='white', fg='black', highlightthickness=1)
email_entry.insert(0, 'mikebyers24@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2, pady=5)

password_label = Label(text="Password:", bg='white', fg='black')
password_label.grid(column=0, row=3, pady=5)

password_entry = Entry(width=23, bg='white', fg='black', highlightthickness=1)
password_entry.grid(column=1, row=3, pady=5)

generate_button = Button(text='Generate', highlightbackground='white', highlightthickness=1, command=generate_my_password)
generate_button.grid(column=2, row=3, pady=4)

add_button = Button(text='Add', width=34, highlightbackground='white', highlightthickness=1, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
