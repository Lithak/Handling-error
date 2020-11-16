from tkinter import *
from tkinter import messagebox

Window = Tk()
Window.geometry('400x200')
Window.title('ERROR CHECKS')
Window.config(background='#7F6A7F')

labelling = Label()


def verify():
    messagebox.showinfo("you guys are crazy")
    mycheck = Button(Window, text="check status", command=verify)
    mycheck.pack()


def check():
    try:
        entry_get = int(check_entry.get())
        if entry_get > 3000:
            messagebox.showinfo("Qualify", 'You qualify for the Malaysia trip. Congratulations.')
            check_entry.delete(0, END)

        else:
            messagebox.showinfo("Qualify", 'You need more funds')
            check_entry.delete(0, END)

    except ValueError:
        messagebox.showinfo("Quality", 'Please deposit more funds for this excursion')


check_account = Label(Window, text="Please enter amount in your account", bg='#7F6A7F')
check_account.pack()

check_entry = Entry(Window, textvariable="")
check_entry.pack()

mybutton = Button(Window, text="Check qualfication ", bg="magenta", command=check).pack()

Window.mainloop()
