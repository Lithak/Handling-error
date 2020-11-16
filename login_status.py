from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("LOGIN PAGE")
window.config(background='#7F6A7F')

user_lbl = Label(window, text="Username", background='#7F6A7F')
user_lbl.pack()

user_entry = Entry(window, textvariable="username")
user_entry.pack()

pass_lbl = Label(window, text="Password", background='#7F6A7F')
pass_lbl.pack()

pass_entry = Entry(window, textvariable="password", show="*")
pass_entry.pack()


def check():
    all_login = {"litha": "0000", "mawande": "1234", "odwa": "4321"}
    my_user = user_entry.get()
    password = pass_entry.get()
    if (my_user, password) in all_login.items():
        messagebox.showinfo("INFO", "Correct Login")
        window.withdraw()
        import CheckingLog
        CheckingLog.verify()
    else:
        messagebox.showinfo("INFO", "Incorrect Login")
        user_entry.delete(0, END)
        pass_entry.delete(0, END)


mybutton = Button(window, text="Login ", bg="magenta", background='#f9bbf9', command=check).pack()

window.mainloop()
