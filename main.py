from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
bg_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', bg='white', fg='black')
website_label.grid(column=0, row=1)

website_entry = Entry(width=35, bg='white', fg='black', highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text='Email/Username:', bg='white', fg='black')
email_label.grid(column=0, row=2)

email_entry = Entry(width=35, bg='white', fg='black', highlightthickness=1)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg='white', fg='black')
password_label.grid(column=0, row=3)

password_entry = Entry(width=23, bg='white', fg='black', highlightthickness=1)
password_entry.grid(column=1, row=3)

generate_button = Button(text='Generate', highlightbackground='white', highlightthickness=1)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=34, highlightbackground='white', highlightthickness=1)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
