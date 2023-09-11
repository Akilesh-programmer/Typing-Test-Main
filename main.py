from start import start
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

# TODO: Find some way to insist user to install pyqt5, mysql-connector-python, mysql, you are going to launch as app
#  so in the readme file say that python have to be installed, then you can itself install the other libraries
#  required for the program to run via the exe file itself
# TODO: Think about launching as an app
# TODO: Think about giving sounds
# TODO: Open new window for every step, normal flow from start to login or sign up to options window to execute the
#   thing to again options, no need of buttons to go to specific pages
# TODO: Separate out the calculation functions, database work functions, PyQt based functions in separate files.

# TODO: Start in one file, login in one file, signup in one file, logged in options in one file
#  general practice in one file, show data in one file special practice in one file, database related things
#  in one or two files, calculations in separate file, constants in separate file
# TODO: Actually no problem if you import same more than once in many files because python just occupies memory only
#   only once and the same will be reused for all files, remember to say this to Rashid Sir.
# TODO: You will be reusing the last 3 steps code in general practice for special practice also, so be sure to make
#   them separate functions
# TODO: Tell the user that there are functions to modify the text
# TODO: Tackle a way to tell the user if they have typed extra words and insist that results won't be correct
#  or it may even create an error, so be careful about that by creating a try except block in list iteration
# TODO: Reset the test id to 0 and then do final commit to github
