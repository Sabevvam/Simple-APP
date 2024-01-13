import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Добавляю текст
        self.setWindowTitle("Persona 6")
        #Змінив розмір вікна
        self.resize(400, 300)

        # set Vertical layout
        # QV - коли хочу вертикальний
        # QH - коли хочу горизонтально
        self.setLayout(qtw.QVBoxLayout())

        # Змінено на self.my_label, щоб зробити його доступним у всьому класі
        self.my_label = qtw.QLabel("Привіт! Як тебе звати?")
        self.layout().addWidget(self.my_label)
        # Зміна розміру шрифта label
        self.my_label.setFont(qtg.QFont('Hello World!', 18))

        # Створення рядка вводу (entry box)
        # Змінено на self.my_entry
        self.my_entry = qtw.QLineEdit()
        self.my_entry.setObjectName("name_field")
        self.my_entry.setText("")
        self.layout().addWidget(self.my_entry)

        # Створення кнопки
        my_button = qtw.QPushButton("Відповісти!", clicked=lambda: self.press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

    def press_it(self):
        # Add name to label
        self.my_label.setText(f'Привіт {self.my_entry.text()}!')
        # Очистка поля вводу
        self.my_entry.clear()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()

