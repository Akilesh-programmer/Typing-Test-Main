import os
from start import start

try:
    global msc
    import mysql.connector as msc
    
except ModuleNotFoundError:
    os.system('pip install mysql-connector-python')
    
    import mysql.connector as msc


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
    

def main():
    create_database()
    create_user_table()
    create_typing_test_data_table()
    start()


if __name__ == '__main__':
    main()


# TODO Add title to the graph plotter window
# TODO Set common title to the graph plotter window
# TODO Reduce the number of words to be typed in the typing test
# TODO Try to show the user how many more words they have to type
# TODO Make the main program error free, it should download the needed libraries if they are not present
# TODO Error will even come when you are trying to install the unpresent library but internet is not there.
# TODO Out app window has to pop up separately as a new icon
# TODO Try to launch it as an app
# TODO Try to show the error for python or mysql itself not present