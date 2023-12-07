from tkinter import *
from constants import *
import random
import time
import mysql.connector as msc
from tkinter import messagebox
from graph_plotter import get_data, plot_graph
import mysql.connector as msc

DISPLAY_TEXT_FONT = ('Helvetica', 14, 'bold')
LABEL_GRID_ROW = 0
LABEL_FONT = ('Helvetica', 18)
LABEL_X = 10

typing_data = []
can_run = True


def calculate_accuracy(typing_data_p):
    correct_words = 0
    wrong_words = 0

    for i in typing_data_p:
        actual_words = i[0].split()
        typed_words = i[1].split()

        for j in range(10):
            if actual_words[j] == typed_words[j]:
                correct_words += 1
            else:
                wrong_words += 1

    accuracy = (correct_words / 50) * 100
    return round(accuracy, 2)


def typing_test(username):
    global can_run
    words = generate_text_list()
    start_time = time.time()
    times_running = 0
    while get_text_generated_count() < 5 and can_run:
        times_running += 1
        show_test_window(generate_line(words), username)

        current_count = get_text_generated_count()
        set_text_generated_count(current_count + 1)
    set_text_generated_count(0)
    finish_time = time.time()

    time_elapsed = int(finish_time - start_time)  # In seconds

    wpm = calculate_wpm(time_elapsed)
    accuracy = calculate_accuracy(typing_data)

    if len(typing_data) == 5 and can_run:
        insert_data(username, wpm, accuracy)
        show_result(wpm, accuracy, username)
    elif not can_run:
        can_run = True
        typing_data.clear()
        home(username)


def generate_text_list():
    fp = open('text.txt', 'r')
    data = fp.read()
    data = data.split()
    return data


def calculate_wpm(time_elapsed):
    # 100 because there are 10 words in each line and 10 times lines are generated
    # Multiplying by 60 for a minute
    return int((50 / time_elapsed) * 60)


def generate_line(words):
    line = ''
    for i in range(10):
        line += str(random.choice(words)) + ' '
    return line


def show_test_window(line, username):
    win = Tk()
    win.title('Typing Test')
    win.configure(width=1500,
                  height=200)
    win.configure(bg=BG)
    win.resizable(False, False)

    # Icon
    icon = PhotoImage(file=KEYBOARD_ICON_LOC)
    win.iconphoto(False, icon)

    # Labels
    label = Label(win,
                  text=line,
                  bg=BG,
                  fg='black',
                  font=DISPLAY_TEXT_FONT)
    label.pack(side=TOP,
               expand=True,
               fill=BOTH)

    # Entry Box
    entry_box = Entry(win)
    entry_box.pack(side=TOP,
                   expand=True,
                   fill=BOTH,
                   padx=10)
    entry_box.focus_force()

    # Submit button
    submit_btn = Button(win,
                        text='Submit',
                        height=1,
                        width=6,
                        font=('Helvetica', 15),
                        bg=WIDGET_BG,
                        fg=WIDGET_FG,
                        command=lambda: submit_btn_clicked(win, line, entry_box, username))
    submit_btn.pack(side=TOP,
                    expand=False,
                    pady=3)
    win.bind('<Return>',
             lambda event: submit_btn_clicked(win, line, entry_box, username))

    win.mainloop()


def submit_btn_clicked(win, generated_line, entry_box, username):
    global can_run
    user_typed = entry_box.get()
    win.destroy()
    if len(user_typed.split()) == 10:
        typing_data.append([generated_line, user_typed])
    else:
        messagebox.showwarning('Invalid number of words',
                               'You have typed extra or no words\nSorry for the inconvenience but the results wont be accurate with incorrect number of words.')
        can_run = False


def show_result(wpm, accuracy, username):
    win = Tk()
    win.title('Result')
    win.configure(width=250,
                  height=175)
    win.configure(bg=BG)
    win.resizable(False, False)
    win.focus_force()

    # Icon
    icon = PhotoImage(file=KEYBOARD_ICON_LOC)
    win.iconphoto(False, icon)

    # Label which displays the text 'WPM: '
    wpm_text_l = Label(win,
                       text='WPM: ',
                       bg=BG,
                       fg=WIDGET_FG,
                       font=LABEL_FONT)
    wpm_text_l.grid(row=0,
                    column=0)

    # Label which displays the text 'Accuracy: '
    accuracy_text_l = Label(win,
                            text='Accuracy: ',
                            bg=BG,
                            fg=WIDGET_FG,
                            font=LABEL_FONT)
    accuracy_text_l.grid(row=1,
                         column=0)

    # WPM label which shows the WPM data
    wpm_l = Label(win,
                  text=wpm,
                  bg=BG,
                  fg=WIDGET_FG,
                  font=LABEL_FONT)
    wpm_l.grid(row=0,
               column=1)

    # WPM label which shows the accuracy data
    accuracy_l = Label(win,
                       text=accuracy,
                       bg=BG,
                       fg=WIDGET_FG,
                       font=LABEL_FONT)
    accuracy_l.grid(row=1,
                    column=1)

    # Close button
    close_btn = Button(win,
                       text='Submit',
                       height=1,
                       font=('Helvetica', 15),
                       bg=WIDGET_BG,
                       fg=WIDGET_FG,
                       command=lambda: close_btn_clicked(username, win))

    win.bind('<Return>',
             lambda event: close_btn_clicked(username, win))
    close_btn.grid(row=2, column=0, columnspan=True, padx=10)

    def close_btn_clicked(username_r, win_r):
        win_r.destroy()
        typing_data.clear()
        home(username_r)

    win.mainloop()


def test_id_generator():
    fp = open('last_test_id.txt', 'r+')
    data = fp.read()

    previous_id = int(data)
    next_id = previous_id + 1

    fp.seek(0, 0)
    fp.write(str(next_id))
    fp.close()

    return next_id


def get_text_generated_count():
    fp = open('text_generated_count.txt', 'r+')
    data = fp.read()
    count = int(data)
    return count


def set_text_generated_count(count):
    fp = open('text_generated_count.txt', 'w')
    fp.write(str(count))
    fp.close()


def insert_data(username, wpm, accuracy):
    test_id = test_id_generator()

    connection = msc.connect(host='localhost',
                             user='root',
                             password='ADMIN',
                             database='Typing_Test')
    cursor = connection.cursor()

    cursor.execute("""
                    INSERT INTO TEST_DATA VALUES(%d, '%s', '%s', '%s');
    """ % (test_id, username, wpm, accuracy))

    connection.commit()
    connection.close()


# ----------------------------------------------------HOME--------------------------------------------------------------
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
                    command=lambda: show_data_btn_clicked(win, username))
    sd_btn.place(x=240,
                 y=BTN_Y)

    win.mainloop()


def typing_test_btn_clicked(win, username):
    win.destroy()
    typing_test(username)


def show_data_btn_clicked(win, username):
    win.destroy()
    plot_graph(get_data(username))
    home(username)
