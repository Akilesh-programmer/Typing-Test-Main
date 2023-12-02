from start import start
import mysql.connector as msc
import os
from tkinter import *
from tkinter import messagebox


def create_database():
    try:
        connection = msc.connect(host='localhost',
                                 user='root',
                                 password='ADMIN')
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE TYPING_TEST;")

        connection.commit()
        connection.close()
    except:
        pass


def create_user_table():
    try:
        connection = msc.connect(host='localhost',
                                 user='root',
                                 password='ADMIN',
                                 database='TYPING_TEST')
        cursor = connection.cursor()

        cursor.execute("""
                        CREATE TABLE USER(
                            USERNAME VARCHAR(255) PRIMARY KEY,
                            PASSWORD VARCHAR(255)
                        );
        """)

        connection.commit()
        connection.close()
    except:
        pass


def create_typing_test_data_table():

    try:
        connection = msc.connect(host='localhost',
                                 user='root',
                                 password='ADMIN',
                                 database='TYPING_TEST')
        cursor = connection.cursor()

        cursor.execute("""
                        CREATE TABLE TEST_DATA(
                            TEST_ID INT PRIMARY KEY,
                            USERNAME VARCHAR(255),
                            WPM INT,
                            ACCURACY FLOAT(5,2),
                            FOREIGN KEY(USERNAME) REFERENCES USER(USERNAME)
                        );
        """)

        connection.commit()
        connection.close()
    except:
        pass
    
def library_installation_commands_and_user_prompt_for_python_mysql_installation():
    fp = open('program_running_times_count', 'r+')
    data = fp.read()
    for i in data:
        if int(i) == 0:
            
            win = Tk()
            label = Label(win, text = 'Please close this window')
            label.pack()
            messagebox.showinfo('Information', 'Make sure that you have python and mysql installed in your device')
            win.mainloop()
            
            os.system('pip install mysql-connector-python')
            os.system('pip install matplotlib')
            os.system('pip install numpy')
            os.system('pip install tk')

            fp.seek(0, 0)
            fp.write('1')
    


def main():
    create_database()
    create_user_table()
    create_typing_test_data_table()
    library_installation_commands_and_user_prompt_for_python_mysql_installation()
    start()


if __name__ == '__main__':
    main()
