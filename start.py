from tkinter import *
from constants import *
from login import login
from signup import signup

BTN_Y = 60
BTN_WIDTH = 6
BTN_HEIGHT = 1
BTN_FONT = ('Helvetica', 20)


def start():
    win = Tk()
    win.title('Typing Test')
    win.configure(width=250,
                  height=175)
    win.configure(bg=BG)
    win.resizable(False, False)

    # Icon
    icon = PhotoImage(file=KEYBOARD_ICON_LOC)
    win.iconphoto(False, icon)

    # Log In Button
    login_btn = Button(win, text='Log In',
                       height=BTN_HEIGHT,
                       width=BTN_WIDTH,
                       font=BTN_FONT,
                       bg=WIDGET_BG,
                       fg=WIDGET_FG,
                       command=lambda: login_btn_click(win))
    login_btn.place(x=15,
                    y=BTN_Y)

    # Sign Up Button
    signup_btn = Button(win,
                        text='Sign Up',
                        height=BTN_HEIGHT,
                        width=BTN_WIDTH,
                        font=BTN_FONT,
                        bg=WIDGET_BG,
                        fg=WIDGET_FG, command=lambda: signup_btn_click(win))
    signup_btn.place(x=130,
                     y=BTN_Y)

    win.mainloop()


def login_btn_click(win):
    win.destroy()
    login()


def signup_btn_click(win):
    win.destroy()
    signup()
