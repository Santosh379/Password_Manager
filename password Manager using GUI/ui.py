from tkinter import *
from gif import Gif
from pass_gen import password_gen
from logic import add,search



LABEL_FONT = ("Segoe UI", 10, "bold")
ENTRY_FONT = ("Segoe UI", 10)
BUTTON_FONT = ("Segoe UI", 10)


def ui_setup(window):
    window.title('Password Manager')
    window.config(bg='#e6eff7', padx=30, pady=20)


    # Add animated GIF
    gif = Gif(window=window, gif_path='assets/shield.gif', size=(180, 180))
    gif.label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    # Labels
    website_label = Label(text='Website:', bg='#e6eff7', fg='#1f2d3d', font=LABEL_FONT)
    website_label.grid(row=1, column=0, sticky='E', pady=5)

    email_label = Label(text='Email/Username:', bg='#e6eff7', fg='#1f2d3d', font=LABEL_FONT)
    email_label.grid(row=2, column=0, sticky='E', pady=5)

    password_label = Label(text='Password:', bg='#e6eff7', fg='#1f2d3d', font=LABEL_FONT)
    password_label.grid(row=3, column=0, sticky='E', pady=5)

    # Entry Fields
    website_entry = Entry(bg='#fafdff', fg='#1f2d3d', font=ENTRY_FONT, width=30)
    website_entry.grid(row=1, column=1, pady=5)
    website_entry.focus()

    email_entry = Entry(bg='#fafdff', fg='#1f2d3d', font=ENTRY_FONT, width=30)
    email_entry.insert(0, string='python@gmail.com')
    email_entry.grid(row=2, column=1, columnspan=2, sticky='W', pady=5)

    password_entry = Entry(bg='#fafdff', fg='#1f2d3d', font=ENTRY_FONT, width=30)
    password_entry.grid(row=3, column=1, pady=5)

    # Button Style
    button_args = {
        'bg': '#357EDD',
        'fg': 'white',
        'font': BUTTON_FONT,
        'activebackground': '#2a6ac0',
        'activeforeground': 'white'
    }

    # Buttons
    search_button = Button(text='Search', width=10, **button_args,command=lambda : search(website_entry.get()))
    search_button.grid(row=1, column=2, padx=5, sticky='W')

    generate_button = Button(text='Generate Password', width=18, **button_args,
                             command=lambda: password_gen(password_entry))
    generate_button.grid(row=3, column=2, padx=5)

    add_button = Button(text='Add', width=42, **button_args, command=lambda: add(website_entry.get(),email_entry.get(),password_entry.get(),website_entry,password_entry,email_entry))
    add_button.grid(row=4, column=0, columnspan=3, pady=(15, 5))


