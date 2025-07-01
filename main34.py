import sys
import wget
import os
from random import choice
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QPalette, QColor
import random
import hashlib

color_list = ['Indigo', 'SlateBlue', 'DarkSlateBlue', 'DarkMagenta', 'Cornsilk',
              'RosyBrown', 'Chocolate', 'Gray', 'Maroon', 'Teal', 'MediumSlateBlue', 'PowderBlue',
              'ForestGreen', 'LawnGreen', 'Linen', 'DarkSlateGray', 'LightYellow', 'LightSalmon',
              'LightSalmon', 'GreenYellow', 'SeaGreen', 'Khaki', 'Fuchsia', 'PeachPuff', 'OliveDrab']

class HashSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super(HashSelectionDialog, self).__init__(parent)
        layout = QGridLayout()
        algorithms = ["MD5", "SHA256", "SHA512", "SHA1"]
        row = col = 0
        self.buttons = []
        for algo in algorithms:
            btn = QPushButton(algo)
            btn.clicked.connect(lambda _, a=algo.lower(): self.select_algorithm(a))
            layout.addWidget(btn, row, col)
            self.buttons.append(btn)
            col += 1
            if col > 3:
                col = 0
                row += 1
        self.setLayout(layout)

    def select_algorithm(self, algorithm):
        self.algorithm_selected = algorithm
        self.accept()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(850, 500)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('NavajoWhite'))
        self.setPalette(palette)
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.home_button = QPushButton("Изменение цвета")
        self.installers_button = QPushButton("Установщики")
        self.hashing_button = QPushButton("Хеширование")
        self.randomizer_button = QPushButton("Рандомайзер")

        for btn in [self.home_button, self.installers_button, self.hashing_button, self.randomizer_button]:
            btn.setAutoFillBackground(True)
            btn.setStyleSheet(f'background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 5px;')

        button_layout.addWidget(self.home_button)
        button_layout.addWidget(self.installers_button)
        button_layout.addWidget(self.hashing_button)
        button_layout.addWidget(self.randomizer_button)

        main_layout.addLayout(button_layout)

        self.current_screen = QLabel("Привет, " + os.getlogin())
        self.current_screen.move(100, 500)
        self.current_screen.setStyleSheet('font-size: 20px')
        main_layout.addWidget(self.current_screen)

        self.home_button.clicked.connect(lambda: self.change_page("Изменение цвета"))
        self.installers_button.clicked.connect(lambda: self.installers())
        self.hashing_button.clicked.connect(lambda: self.hashing())
        self.randomizer_button.clicked.connect(lambda: self.randomize())

        self.setLayout(main_layout)

    def change_page(self, page_name):
        active_btn = None
        all_buttons = [self.home_button, self.installers_button, self.hashing_button, self.randomizer_button]

        for btn in all_buttons:
            if btn.text() == page_name:
                active_btn = btn
                btn.setStyleSheet('background-color: BlanchedAlmond; font-size: 16px; padding: 10px; border-radius: 5px;')
            else:
                btn.setStyleSheet('background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 5px;')

        if page_name == "Изменение цвета":
            bg_color = choice(color_list)
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor(bg_color))
            self.setPalette(palette)
            text = f"Цвет фона изменился на {bg_color}"

        self.current_screen.setText(text)

    def installers(self):
        self.current_screen.setText("")
        self.label = QLabel('Anydesk', self)
        self.label.setStyleSheet('font-size: 20px')
        self.label.move(20, 100)
        self.label.show()
        self.btn_anydesk = QPushButton('Скачать', self)
        self.btn_anydesk.resize(130, 40)
        self.btn_anydesk.setStyleSheet('background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 8px;')
        self.btn_anydesk.clicked.connect(self.anydesk)
        self.btn_anydesk.move(100, 100)
        self.btn_anydesk.show()

        self.label1 = QLabel('Chrome', self)
        self.label1.setStyleSheet('font-size: 20px')
        self.label1.move(20, 200)
        self.label1.show()
        self.btn_chrome = QPushButton('Скачать', self)
        self.btn_chrome.resize(130, 40)
        self.btn_chrome.setStyleSheet('background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 8px;')
        self.btn_chrome.clicked.connect(self.chrome)
        self.btn_chrome.move(100, 200)
        self.btn_chrome.show()

    def anydesk(self):
        url = "https://github.com/zxcsovamb/m9snoi/raw/refs/heads/main/anydesk.exe"
        wget.download(url, out=f"C:/Users/{os.getlogin()}/AppData/Local/Temp/anydesk.exe")
        self.anydesk1 = QPushButton('Открыть', self)
        self.anydesk1.resize(130, 40)
        self.anydesk1.setStyleSheet('background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 8px;')
        self.anydesk1.clicked.connect(self.anydesk_open)
        self.anydesk1.move(250, 100)
        self.anydesk1.show()

    def chrome(self):
        url = "https://github.com/zxcsovamb/midnight/raw/refs/heads/main/ChromeSetup.exe"
        wget.download(url, out=f"C:/Users/{os.getlogin()}/AppData/Local/Temp/ChromeSetup.exe")
        self.btn_chrome1 = QPushButton('Открыть', self)
        self.btn_chrome1.setStyleSheet('background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 8px;')
        self.btn_chrome1.clicked.connect(self.chrome_open)
        self.btn_chrome1.move(250, 200)
        self.btn_chrome1.resize(130, 40)
        self.btn_chrome1.show()

    def chrome_open(self):
        os.system(f"C:/Users/{os.getlogin()}/AppData/Local/Temp/ChromeSetup.exe")

    def anydesk_open(self):
        os.system(f"C:/Users/{os.getlogin()}/AppData/Local/Temp/anydesk.exe")

    def hashing(self):
        self.clear_screen()
        input_field = QLineEdit(self)
        input_field.setPlaceholderText("Введите строку для хэширования...")
        input_field.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; background-color: WhiteSmoke;')
        input_field.resize(400, 40)
        input_field.move(225, 100)
        input_field.show()

        submit_button = QPushButton("Выбрать алгоритм", self)
        submit_button.setStyleSheet('background-color: BurlyWood; font-size: 16px; padding: 10px; border-radius: 5px;')
        submit_button.resize(170, 40)
        submit_button.move(340, 160)
        submit_button.clicked.connect(lambda: self.open_hash_selection(input_field.text()))
        submit_button.show()

    def open_hash_selection(self, data_to_hash):
        dialog = HashSelectionDialog(self)
        result = dialog.exec_()
        if result == QDialog.Accepted and hasattr(dialog, 'algorithm_selected'):
            self.calculate_hash(data_to_hash, dialog.algorithm_selected)

    def calculate_hash(self, data, algorithm):
        try:
            if algorithm == "md5":
                hashed_data = hashlib.md5(data.encode()).hexdigest()
            elif algorithm == "sha256":
                hashed_data = hashlib.sha256(data.encode()).hexdigest()
            elif algorithm == "sha512":
                hashed_data = hashlib.sha512(data.encode()).hexdigest()
            elif algorithm == "sha1":
                hashed_data = hashlib.sha1(data.encode()).hexdigest()
            else:
                raise ValueError("Алгоритм не поддерживается.")

            clipboard = QApplication.clipboard()
            clipboard.setText(hashed_data)

            QMessageBox.information(self, "Результат хэширования",
                                     f"Использован алгоритм: {algorithm.upper()} \n\n"
                                     f"Хэш-код:\n{hashed_data} \n\n"
                                     f"Значение хэша скопировано!",
                                     QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e), QMessageBox.Ok)

    def clear_screen(self):
        children = self.findChildren((QLabel, QPushButton, QLineEdit))
        for child in children:
            child.deleteLater()

    def randomize(self):
        asd = str(random.randint(1, 9999999999))
        dlg = QMessageBox(self)
        dlg.setWindowTitle(asd)
        dlg.setText("Число: "+asd+" Скопировать?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Окно")
            dlg.setText("Успешно!")
            dlg.setIcon(QMessageBox.Information)
            button = dlg.exec()

            if button == QMessageBox.Ok:
                ...
            clipboard = QApplication.clipboard()
            clipboard.setText(asd)
        else:
            ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())