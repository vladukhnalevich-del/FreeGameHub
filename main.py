import sys
from PyQt5.QtWidgets import QApplication, QDialog
from modules.registration import Registration
from modules.mainwindow import FreeGameHub


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Установка стилей для сообщений
    app.setStyleSheet("""
        QMessageBox {
            background-color: #3a3a3a;
            color: #ffffff;
        }
        QMessageBox QLabel {
            color: #ffffff;
        }
        QMessageBox QPushButton {
            background-color: #4a9eff;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            padding: 8px 15px;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background-color: #5aaaff;
        }
    """)

    # Запуск регистрации
    reg = Registration()
    if reg.exec_() == QDialog.Accepted:
        window = FreeGameHub(reg.user_data)
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()