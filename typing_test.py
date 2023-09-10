from tkinter import *
from constants import *
import random
import time

DISPLAY_TEXT_FONT = ('Helvetica', 14)
LABEL_GRID_ROW = 0

typing_data = []


def calculate_accuracy(typing_data_p):
    correct_words = 0
    wrong_words = 0

    for i in typing_data_p:
        actual_words = i[0].split()
        typed_words = i[1].split()

        print(actual_words)
        print(typed_words)

        for j in range(10):
            if actual_words[j] == typed_words[j]:
                correct_words += 1
            else:
                wrong_words += 1

    print(correct_words, wrong_words)


def typing_test(username):
    words = generate_text_list()
    start_time = time.time()
    while get_text_generated_count() < 1:
        show_test_window(generate_line(words))

        current_count = get_text_generated_count()
        set_text_generated_count(current_count + 1)
    set_text_generated_count(0)
    finish_time = time.time()

    time_elapsed = int(finish_time - start_time)  # In seconds
    print('Your WPM is', calculate_wpm(time_elapsed))
    print('Your accuracy is', calculate_accuracy(typing_data))


def generate_text_list():
    fp = open('text.txt', 'r')
    data = fp.read()
    data = data.split()
    return data


def calculate_wpm(time_elapsed):
    # 100 because there are 10 words in each line and 10 times lines are generated
    # Multiplying by 60 for a minute
    return int((10 / time_elapsed) * 60)


def generate_line(words):
    line = ''
    for i in range(10):
        line += str(random.choice(words)) + ' '
    return line


def show_test_window(line):
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
                  fg=WIDGET_FG,
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
                        command=lambda: submit_btn_clicked(win, line, entry_box))
    submit_btn.pack(side=TOP,
                    expand=False,
                    pady=3)
    win.bind('<Return>',
             lambda event: submit_btn_clicked(win, line, entry_box))

    win.mainloop()


def submit_btn_clicked(win, generated_line, entry_box):
    user_typed = entry_box.get()
    win.destroy()
    typing_data.append([generated_line, user_typed])


def show_result():
    pass


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


def insert_data():
    pass


typing_test('Akilesh')
