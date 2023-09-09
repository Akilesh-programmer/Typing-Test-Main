import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
