import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from utils.validators import validate_password_strength


class Registration(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FreeGameHub - Регистрация")
        self.setFixedSize(900, 900)
        self.user_data = None
        self.init_ui()
        self.setup_styles()

    def setup_styles(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #2c2c2c;
            }
            QLabel {
                color: #ffffff;
                font-weight: 500;
            }
            QLineEdit {
                background-color: #3a3a3a;
                color: #ffffff;
                border: 1px solid #5a5a5a;
                border-radius: 6px;
                padding: 10px;
                font-size: 14px;
                selection-background-color: #4a9eff;
            }
            QLineEdit:focus {
                border-color: #4a9eff;
                background-color: #444444;
            }
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #5aaaff;
            }
            QPushButton:pressed {
                background-color: #3a8aee;
            }
        """)

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(25, 25, 25, 25)

        # Логотип и заголовок
        title_container = QWidget()
        title_layout = QVBoxLayout(title_container)
        title_layout.setAlignment(Qt.AlignCenter)

        icon_label = QLabel("🎮")
        icon_label.setStyleSheet("font-size: 48px; margin-bottom: 5px;")
        icon_label.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(icon_label)

        title = QLabel("FreeGameHub")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(title)

        subtitle = QLabel("Создайте аккаунт для начала")
        subtitle.setFont(QFont("Segoe UI", 9))
        subtitle.setStyleSheet("color: #aaaaaa;")
        subtitle.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(subtitle)

        layout.addWidget(title_container)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #5a5a5a; margin: 15px 0;")
        layout.addWidget(separator)

        # Поля ввода
        self.name_input = QLineEdit()
        self.login_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.confirm_input = QLineEdit()

        fields = [
            ("Имя пользователя", self.name_input),
            ("Логин", self.login_input),
            ("Пароль", self.pass_input),
            ("Подтвердите пароль", self.confirm_input)
        ]

        for label_text, field in fields:
            label = QLabel(label_text)
            label.setStyleSheet("margin-top: 8px;")
            layout.addWidget(label)

            if "Пароль" in label_text:
                field.setEchoMode(QLineEdit.Password)
                field.setPlaceholderText("Минимум 8 символов, заглавные, цифры, спецсимволы")
            else:
                field.setPlaceholderText(f"Введите {label_text.lower()}")

            layout.addWidget(field)

        # Информация о пароле
        pass_info = QLabel(
            "Пароль должен содержать: минимум 8 символов, заглавные и строчные буквы, цифры, специальные символы (!@#$%^&*)")
        pass_info.setStyleSheet("color: #888888; font-size: 11px; margin: 5px 0 15px 0;")
        pass_info.setAlignment(Qt.AlignCenter)
        pass_info.setWordWrap(True)
        layout.addWidget(pass_info)

        # Кнопка регистрации
        btn = QPushButton("Создать аккаунт")
        btn.clicked.connect(self.register)
        btn.setCursor(Qt.PointingHandCursor)
        layout.addWidget(btn)

        # Статус регистрации
        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setWordWrap(True)
        self.status.setMinimumHeight(50)
        layout.addWidget(self.status)

        self.setLayout(layout)

    def register(self):
        name = self.name_input.text().strip()
        login = self.login_input.text().strip()
        password = self.pass_input.text()
        confirm = self.confirm_input.text()

        # Валидация
        errors = []
        if not name:
            errors.append("Введите имя")
        elif len(name) < 2:
            errors.append("Имя должно содержать минимум 2 символа")

        if not login:
            errors.append("Введите логин")
        elif len(login) < 3:
            errors.append("Логин должен содержать минимум 3 символа")

        if password != confirm:
            errors.append("Пароли не совпадают")
        else:
            # Проверка сложности пароля
            password_errors = validate_password_strength(password)
            if password_errors:
                errors.extend(password_errors)

        if errors:
            self.status.setText("⚠️ " + "\n".join(errors))
            self.status.setStyleSheet("""
                color: #ff6b6b;
                background-color: rgba(255, 107, 107, 0.1);
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ff6b6b;
            """)
            return

        # Успешная регистрация
        self.user_data = {
            "name": name,
            "login": login,
            "password": password,
            "id": f"FGH{random.randint(10000, 99999)}",
            "avatar_emoji": "👤",
            "avatar_color": random.choice(["#4a9eff", "#ff6b6b", "#6bcc78", "#ffb74d"])
        }

        self.status.setText(f"✅ Аккаунт создан успешно!\nВаш ID: {self.user_data['id']}")
        self.status.setStyleSheet("""
            color: #6bcc78;
            background-color: rgba(107, 204, 120, 0.1);
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #6bcc78;
        """)

        # Блокируем кнопку после успешной регистрации
        sender = self.sender()
        if sender:
            sender.setEnabled(False)
            sender.setText("✅ Аккаунт создан")

        # Задержка перед закрытием
        QTimer.singleShot(1500, self.accept)