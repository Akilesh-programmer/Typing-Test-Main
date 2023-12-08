import os

try: 
    global msc
    global plt
    global np
    
    import mysql.connector as msc
    import matplotlib.pyplot as plt
    import numpy as np
    
except ModuleNotFoundError:
    os.system('pip install mysql-connector-python')
    os.system('pip install matplotlib')
    
    import mysql.connector as msc
    import matplotlib.pyplot as plt
    import numpy as np


def get_data(username):
    connection = msc.connect(host = 'localhost',
                            user = 'root',
                            password = 'ADMIN',
                            database = 'typing_test')
    cursor = connection.cursor()
    cursor.execute('''
                    SELECT * FROM TEST_DATA;
                ''')
    data = cursor.fetchall()

    connection.commit()
    connection.close()

    current_user_data = []

    for i in data:
        if i[1] == username:
            current_user_data.append(i)

    return current_user_data


def plot_graph(data):

    # WPM
    n = len(data)
    x_array = []

    for i in range(1, n + 1): # If you don't start from 1, then in graph test number will start from 0
        x_array.append(i)

    y_array = []
    
    for i in data:
        y_array.append(i[2])

    xpoints = np.array(x_array)
    ypoints = np.array(y_array)

    plt.subplot(1, 2, 1)
    plt.plot(xpoints, ypoints, marker = 'o', color = 'g')
    plt.xlabel('Test Number')
    plt.ylabel('WPM')
    plt.grid()

    plt.subplots_adjust(right = 0.9)

    # AVERAGE

    y_array = []
    for i in data:
        y_array.append(i[3])

    ypoints = np.array(y_array)

    plt.subplot(1, 2, 2)
    plt.plot(xpoints, ypoints, marker = 'o', color = 'g')
    plt.xlabel('Test Number')
    plt.ylabel('Accuracy')
    plt.suptitle('Your Progress')
    plt.grid()

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')

    
    plt.show()
