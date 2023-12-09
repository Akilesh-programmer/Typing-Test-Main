from constants import *
from login import login_from_signup
import os
from tkinter import *
from tkinter import messagebox

try:
    global msc
    import mysql.connector as msc

    
except ModuleNotFoundError:
    os.system('pip install mysql-connector-python')
    import mysql.connector as msc


LABEL_X = 0
ENTRY_X = 115
ENTRY_WIDTH = 67
LABEL_FONT = ('Helvetica', 18)
ENTRY_FONT = ('Helvetica', 18)


def signup():
    win = Tk()
    win.title('Sign Up')
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
                       font=ENTRY_FONT,
                       show = '*')
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

    win.mainloop()


def submit_btn_clicked(username_e, password_e, win):
    username = username_e.get()
    password = password_e.get()

    username_e.delete(0, END)
    password_e.delete(0, END)

    if not check_duplication(username):
        insert_into_user(username, password)
        win.destroy()
        login_from_signup()

    else:
        messagebox.showwarning('Username already present',
                               'Choose some other username')
        username_e.focus_force()


def check_duplication(username):
    connection = msc.connect(host='localhost',
                             user='root',
                             password='ADMIN',
                             database='TYPING_TEST')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM USER;')
    data = cursor.fetchall()

    connection.commit()
    connection.close()

    """
        Here I am using the if statement because if the program is being run for the first time in a computer then there
        won't be any data to iterate and it will generate error.
    """
    if len(data) > 0:
        check = False
        for i in data:
            if i[0].lower() == username.lower():
                check = True
        return check
    else:
        return False


def insert_into_user(username, password):
    connection = msc.connect(host='localhost',
                             user='root',
                             password='ADMIN',
                             database='TYPING_TEST')
    cursor = connection.cursor()

    cursor.execute("""
                    INSERT INTO USER VALUES('%s', '%s');
    """ % (username, password))

    connection.commit()
    connection.close()
