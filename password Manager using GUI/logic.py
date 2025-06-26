import json
from json import JSONDecodeError
from tkinter import messagebox


def add(website,email,password,web_entry,password_entry,email_entry):

    new_data = {
        website:{
        'Email': email,
        'Password': password
            }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="You haven't answered all the fields.\nPlease check once again")
    else:
        is_ok = messagebox.askokcancel(title="Your Credentials",
                                   message=f'Here are you credentials for {website}:\n Email: {email}\n Password: {password}\n Are these credentials correct?')
        if is_ok:
            try:
                with open('cred_data.json','r') as file:
                    data = json.load(file)

            except (JSONDecodeError,FileNotFoundError):
                with open('cred_data.json','w') as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)

                with open('cred_data.json','w') as file:
                    json.dump(data,file,indent=4)
            finally:
                web_entry.delete(0,len(website))
                email_entry.delete(0, len(email))
                password_entry.delete(0, len(password))

def search(website):
    try:
        with open('cred_data.json','r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Oops!',message='There are no credentials to search.')
    else:
        matched_key = next((key for key in data if key.lower() == website.lower()), None)

        if matched_key:
            email = data[matched_key]['Email']
            password = data[matched_key]['Password']
            messagebox.showinfo('Credentials',
                                message=f"Here are your Credentials for {matched_key}\n\nEmail: {email}\n\nPassword: {password}")
        else:
            messagebox.showinfo(title='Oops', message=f'No credentials found for {website}')

