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
        connection = msc.connect(host='localhost',
                                 user='root',
                                 password='ADMIN')
        cursor = connection.cursor()
        
        cursor.execute('DROP DATABASE TYPING_TEST;')
        
        connection.commit()
        connection.close()
        
        connection2 = msc.connect(host='localhost',
                                 user='root',
                                 password='ADMIN')
        cursor2 = connection2.cursor()

        cursor2.execute("CREATE DATABASE TYPING_TEST;")

        connection2.commit()
        connection2.close()


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
        
        cursor.execute('''
                       INSERT INTO USER VALUES('one', 'one');
                       ''')

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
        
        prebuilt_values = [(1, 'one', 45, 80.00),
                           (2, 'one', 47, 82.00),
                           (3, 'one', 49, 83.00),
                           (4, 'one', 35, 81.00),
                           (5, 'one', 48, 98.00),
                           ]
        
        for i in prebuilt_values:
            
            cursor.execute('''
                        INSERT INTO TEST_DATA VALUES(%d, '%s', %d, %f);
                        '''%(i[0], i[1], i[2], i[3]))

        connection.commit()
        connection.close()
    except:
        pass
    

def main():
    fp = open('number_of_running_in_this_computer', 'r+')
    data = fp.read()
    if not int(data):
        create_database()
        create_user_table()
        create_typing_test_data_table()
        fp.seek(0, 0)
        fp.write('1')
    fp.close()
    
    start()


if __name__ == '__main__':
    main()
