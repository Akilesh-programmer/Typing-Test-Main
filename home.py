from tkinter import *
from constants import *
from typing_test import typing_test

BTN_HEIGHT = 1
BTN_WIDTH = 13
BTN_FONT = ('Helvetica', 20)
BTN_Y = 20


def home(username):
    win = Tk()
    win.title('Home')
    win.configure(width=475,
                  height=100)
    win.configure(bg=BG)
    win.resizable(False, False)
    win.focus_force()

    # Icon
    icon = PhotoImage(file=KEYBOARD_ICON_LOC)
    win.iconphoto(False, icon)

    # General practice button
    gp_btn = Button(win,
                    text='Typing Test',
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    font=BTN_FONT,
                    bg=WIDGET_BG,
                    fg=WIDGET_FG,
                    command=lambda: typing_test_btn_clicked(win, username))
    gp_btn.place(x=10,
                 y=BTN_Y)

    # Show Data button
    sd_btn = Button(win,
                    text='Show Data',
                    height=BTN_HEIGHT,
                    width=BTN_WIDTH,
                    font=BTN_FONT,
                    bg=WIDGET_BG,
                    fg=WIDGET_FG,
                    command=lambda: show_data_btn_clicked(win))
    sd_btn.place(x=240,
                 y=BTN_Y)

    win.mainloop()


def typing_test_btn_clicked(win, username):
    win.destroy()
    typing_test(username)


def show_data_btn_clicked(win):
    win.destroy()
    print('Show Data button clicked')
