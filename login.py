from tkinter import *
from constants import *
import mysql.connector as msc
from tkinter import messagebox
from home import home


LABEL_X = 0
ENTRY_X = 115
ENTRY_WIDTH = 67
LABEL_FONT = ('Helvetica', 18)
ENTRY_FONT = ('Helvetica', 18)


def login():
    win = Tk()
    win.title('Login')
    win.configure(width=1000,
                  height=155)
    win.configure(bg=BG)
    win.resizable(False, False)

    # Icon
    icon = PhotoImage(file=KEYBOARD_ICON_LOC)
    win.iconphoto(False, icon)

    # Username label
    username_l = Label(win,
                       text='Username',
                       bg=BG,
                       fg=WIDGET_FG,
                       font=LABEL_FONT)
    username_l.place(x=LABEL_X,
                     y=10)

    # Password label
    password_l = Label(win,
                       text='Password',
                       bg=BG,
                       fg=WIDGET_FG,
                       font=LABEL_FONT)
    password_l.place(x=LABEL_X,
                     y=60)

    # Username Entry
    username_e = Entry(win,
                       width=ENTRY_WIDTH,
                       font=ENTRY_FONT)
    username_e.place(x=ENTRY_X,
                     y=10)
    username_e.focus_force()

    # Password Entry
    password_e = Entry(win,
                       width=ENTRY_WIDTH,
                       font=ENTRY_FONT)
    password_e.place(x=ENTRY_X,
                     y=60)

    # Submit button
    submit_btn = Button(win,
                        text='Submit',
                        height=1,
                        width=6,
                        font=('Helvetica', 15),
                        bg=WIDGET_BG,
                        fg=WIDGET_FG,
                        command=lambda: submit_btn_clicked(username_e, password_e, win))
    submit_btn.place(x=475,
                     y=110)

    win.bind('<Return>',
             lambda event: submit_btn_clicked(username_e, password_e, win))


def submit_btn_clicked(username_e, password_e, win):
    username = username_e.get()
    password = password_e.get()

    username_e.delete(0, END)
    password_e.delete(0, END)

    if check_details(username, password) == 1:
        win.destroy()
        home(username)
    elif check_details(username, password) == 0:
        messagebox.showwarning('No Match Found',
                               'Recheck and enter your details correctly')
        username_e.focus_force()
    elif check_details(username, password) == 2:
        messagebox.showwarning('Database Empty',
                               'Please signup first and then log in')
        win.destroy()


def check_details(username, password):
    connection = msc.connect(host='localhost',
                             user='root',
                             password='ADMIN',
                             database='TYPING_TEST')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM USER;")

    data = cursor.fetchall()

    connection.commit()
    connection.close()

    """
        First we want to check if there is some data so that we can compare it, if the program is being run for the 
        first time then no one would have signed up so first we are going to check if someone has signed up
    """

    if len(data) > 0:
        check = 0
        for i in data:
            if i[0].lower() == username.lower() and i[1] == password:
                check = 1
        return check
    else:
        return 2
