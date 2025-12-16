from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont


class ProfileTab(QWidget):
    def __init__(self, user_data, main_window):
        super().__init__()
        self.user_data = user_data
        self.main_window = main_window
        self.checkboxes = []  # Добавляем атрибут для чекбоксов
        self.init_ui()

    def init_ui(self):
        """Инициализация интерфейса вкладки профиля"""
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        # Заголовок
        title = QLabel("👤 Мой профиль")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #ffffff; margin-bottom: 10px;")
        layout.addWidget(title)

        # Информация о профиле
        profile_frame = QFrame()
        profile_frame.setStyleSheet("""
            QFrame {
                background-color: #3a3a3a;
                border: 1px solid #5a5a5a;
                border-radius: 8px;
            }
        """)

        profile_layout = QVBoxLayout(profile_frame)
        profile_layout.setContentsMargins(20, 20, 20, 20)
        profile_layout.setSpacing(15)

        # Аватар
        avatar_container = QWidget()
        avatar_layout = QVBoxLayout(avatar_container)
        avatar_layout.setAlignment(Qt.AlignCenter)

        self.avatar_label = QLabel(self.user_data['avatar_emoji'])
        self.avatar_label.setStyleSheet(f"""
            font-size: 48px;
            background-color: {self.user_data['avatar_color']};
            border-radius: 50px;
            padding: 25px;
            max-width: 100px;
            max-height: 100px;
        """)
        self.avatar_label.setAlignment(Qt.AlignCenter)
        avatar_layout.addWidget(self.avatar_label)

        # Кнопки для аватара
        avatar_buttons_widget = QWidget()
        avatar_buttons_layout = QHBoxLayout(avatar_buttons_widget)

        change_avatar_btn = QPushButton("👤 Сменить эмодзи")
        change_avatar_btn.setStyleSheet("""
            QPushButton {
                background-color: #444444;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 11px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)
        change_avatar_btn.clicked.connect(self.change_avatar_emoji)
        change_avatar_btn.setCursor(Qt.PointingHandCursor)
        avatar_buttons_layout.addWidget(change_avatar_btn)

        change_color_btn = QPushButton("🎨 Сменить фон")
        change_color_btn.setStyleSheet("""
            QPushButton {
                background-color: #444444;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 11px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)
        change_color_btn.clicked.connect(self.change_avatar_color)
        change_color_btn.setCursor(Qt.PointingHandCursor)
        avatar_buttons_layout.addWidget(change_color_btn)

        avatar_layout.addWidget(avatar_buttons_widget)
        profile_layout.addWidget(avatar_container)

        # Данные пользователя
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setSpacing(10)

        fields = [
            ("Имя пользователя", self.user_data['name']),
            ("Логин", self.user_data['login']),
            ("ID аккаунта", self.user_data['id']),
        ]

        for label, value in fields:
            field_widget = QWidget()
            field_layout = QHBoxLayout(field_widget)

            label_widget = QLabel(label)
            label_widget.setStyleSheet("color: #aaaaaa; font-weight: bold; min-width: 120px;")

            value_widget = QLabel(value)
            value_widget.setStyleSheet("color: #ffffff;")

            field_layout.addWidget(label_widget)
            field_layout.addWidget(value_widget)
            field_layout.addStretch()

            info_layout.addWidget(field_widget)

        profile_layout.addWidget(info_widget)
        layout.addWidget(profile_frame)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #5a5a5a; margin: 10px 0;")
        layout.addWidget(separator)

        # Настройки
        settings_label = QLabel("Настройки аккаунта:")
        settings_label.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold;")
        layout.addWidget(settings_label)

        settings = [
            ("🔒 Изменить пароль", self.change_password),
            ("🔔 Настройки уведомлений", self.notification_settings),
            ("🎨 Оформление", self.theme_settings),
            ("🌐 Язык", self.language_settings),
            ("❓ Помощь и поддержка", self.help_support)
        ]

        for setting_text, callback in settings:
            btn = QPushButton(setting_text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #444444;
                    color: #ffffff;
                    border: none;
                    border-radius: 6px;
                    padding: 12px 15px;
                    text-align: left;
                    font-size: 13px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
            """)
            btn.clicked.connect(callback)
            btn.setCursor(Qt.PointingHandCursor)
            layout.addWidget(btn)

        layout.addStretch()
        self.setLayout(layout)

    def change_avatar_emoji(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Выберите эмодзи")
        dialog.setFixedSize(900, 200)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #3a3a3a;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
                font-size: 20px;
                min-width: 50px;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #5aaaff;
            }
        """)

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        label = QLabel("Выберите эмодзи для аватара:")
        label.setStyleSheet("color: #ffffff; font-weight: bold;")
        layout.addWidget(label)

        emoji_widget = QWidget()
        emoji_layout = QHBoxLayout(emoji_widget)
        emoji_layout.setSpacing(10)

        emojis = ["👤", "👨", "👩", "🧑", "👦", "👧", "🦸", "🦹", "🧙", "🧛"]

        for emoji in emojis:
            btn = QPushButton(emoji)
            btn.clicked.connect(lambda checked, e=emoji: self.set_avatar_emoji(e, dialog))
            emoji_layout.addWidget(btn)

        layout.addWidget(emoji_widget)
        dialog.exec_()

    def set_avatar_emoji(self, emoji, dialog):
        self.user_data['avatar_emoji'] = emoji
        self.avatar_label.setText(emoji)
        dialog.accept()

    def change_avatar_color(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Выберите цвет фона")
        dialog.setFixedSize(300, 200)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #3a3a3a;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
                min-width: 50px;
                min-height: 50px;
            }
        """)

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        label = QLabel("Выберите цвет фона для аватара:")
        label.setStyleSheet("color: #ffffff; font-weight: bold;")
        layout.addWidget(label)

        colors_widget = QWidget()
        colors_layout = QHBoxLayout(colors_widget)
        colors_layout.setSpacing(10)

        colors = ["#4a9eff", "#ff6b6b", "#6bcc78", "#ffb74d", "#9c27b0", "#03a9f4", "#ff9800", "#e91e63"]

        for color in colors:
            btn = QPushButton()
            btn.setStyleSheet(f"background-color: {color};")
            btn.clicked.connect(lambda checked, c=color: self.set_avatar_color(c, dialog))
            colors_layout.addWidget(btn)

        layout.addWidget(colors_widget)
        dialog.exec_()

    def set_avatar_color(self, color, dialog):
        self.user_data['avatar_color'] = color
        self.avatar_label.setStyleSheet(f"""
            font-size: 48px;
            background-color: {color};
            border-radius: 50px;
            padding: 25px;
            max-width: 100px;
            max-height: 100px;
        """)
        dialog.accept()

    def change_password(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Изменение пароля")
        dialog.setFixedSize(600, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #3a3a3a;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #444444;
                color: #ffffff;
                border: 1px solid #5a5a5a;
                border-radius: 4px;
                padding: 8px;
            }
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
            }
            QPushButton:hover {
                background-color: #5aaaff;
            }
        """)

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Изменение пароля")
        title.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        # Старый пароль
        old_pass_label = QLabel("Старый пароль:")
        old_pass_label.setStyleSheet("color: #cccccc; margin-top: 10px;")
        layout.addWidget(old_pass_label)

        old_pass_input = QLineEdit()
        old_pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(old_pass_input)

        # Новый пароль
        new_pass_label = QLabel("Новый пароль (минимум 6 символов):")
        new_pass_label.setStyleSheet("color: #cccccc; margin-top: 10px;")
        layout.addWidget(new_pass_label)

        new_pass_input = QLineEdit()
        new_pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(new_pass_input)

        # Подтверждение пароля
        confirm_pass_label = QLabel("Подтвердите новый пароль:")
        confirm_pass_label.setStyleSheet("color: #cccccc; margin-top: 10px;")
        layout.addWidget(confirm_pass_label)

        confirm_pass_input = QLineEdit()
        confirm_pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(confirm_pass_input)

        # Кнопки
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)

        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(dialog.reject)
        buttons_layout.addWidget(cancel_btn)

        save_btn = QPushButton("Сохранить")
        save_btn.clicked.connect(lambda: self.save_new_password(
            old_pass_input.text(),
            new_pass_input.text(),
            confirm_pass_input.text(),
            dialog
        ))
        buttons_layout.addWidget(save_btn)

        layout.addWidget(buttons_widget)
        dialog.exec_()

    def save_new_password(self, old_pass, new_pass, confirm_pass, dialog):
        # Проверка старого пароля
        if old_pass != self.user_data['password']:
            QMessageBox.warning(self, "Ошибка", "Старый пароль введен неверно!")
            return

        # Проверка нового пароля
        if len(new_pass) < 6:
            QMessageBox.warning(self, "Ошибка", "Новый пароль должен содержать минимум 6 символов!")
            return

        if new_pass != confirm_pass:
            QMessageBox.warning(self, "Ошибка", "Новые пароли не совпадают!")
            return

        # Сохранение нового пароля
        self.user_data['password'] = new_pass
        QMessageBox.information(self, "Успех", "Пароль успешно изменен!")
        dialog.accept()

    def notification_settings(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Настройки уведомлений")
        dialog.setFixedSize(600, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #3a3a3a;
            }
            QLabel {
                color: #ffffff;
            }
            QCheckBox {
                color: #ffffff;
                font-size: 14px;
                padding: 5px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:checked {
                background-color: #4a9eff;
                border: 2px solid #5a5a5a;
            }
            QCheckBox::indicator:unchecked {
                background-color: #444444;
                border: 2px solid #5a5a5a;
            }
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
            }
            QPushButton:hover {
                background-color: #5aaaff;
            }
        """)

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Настройки уведомлений")
        title.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        # Настройки уведомлений
        notifications = [
            ("Новые игры", True),
            ("Обновления игр", True),
            ("Акции и скидки", False),
            ("Новости платформы", True),
            ("Рекомендации", True)
        ]

        self.checkboxes = []

        for text, default in notifications:
            checkbox = QCheckBox(text)
            checkbox.setChecked(default)
            self.checkboxes.append((text, checkbox))
            layout.addWidget(checkbox)

        layout.addStretch()

        # Кнопки
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)

        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(dialog.reject)
        buttons_layout.addWidget(cancel_btn)

        save_btn = QPushButton("Сохранить")
        save_btn.clicked.connect(lambda: self.save_notification_settings(dialog))
        buttons_layout.addWidget(save_btn)

        layout.addWidget(buttons_widget)
        dialog.exec_()

    def save_notification_settings(self, dialog):
        settings = {}
        for text, checkbox in self.checkboxes:
            settings[text] = checkbox.isChecked()

        # Здесь можно сохранить настройки в базу данных или файл
        QMessageBox.information(self, "Успех", "Настройки уведомлений сохранены!")
        dialog.accept()

    def theme_settings(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Настройки оформления в разработке")
        msg.setWindowTitle("Оформление")
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #3a3a3a;
                color: #ffffff;
            }
            QMessageBox QLabel {
                color: #ffffff;
            }
        """)
        msg.exec_()

    def language_settings(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Настройки языка в разработке")
        msg.setWindowTitle("Язык")
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #3a3a3a;
                color: #ffffff;
            }
            QMessageBox QLabel {
                color: #ffffff;
            }
        """)
        msg.exec_()

    def help_support(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Помощь и поддержка")
        dialog.setFixedSize(600, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #3a3a3a;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
            }
            QPushButton:hover {
                background-color: #5aaaff;
            }
        """)

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Помощь и поддержка")
        title.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 16px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Контактная информация
        contacts_widget = QWidget()
        contacts_layout = QVBoxLayout(contacts_widget)
        contacts_layout.setSpacing(10)

        phone_label = QLabel("📞 Телефон поддержки:")
        phone_label.setStyleSheet("color: #cccccc; font-weight: bold;")
        contacts_layout.addWidget(phone_label)

        phone_value = QLabel("+375 33 67 31161")
        phone_value.setStyleSheet("color: #4a9eff; font-size: 14px; font-weight: bold;")
        contacts_layout.addWidget(phone_value)

        email_label = QLabel("📧 Email поддержки:")
        email_label.setStyleSheet("color: #cccccc; font-weight: bold; margin-top: 10px;")
        contacts_layout.addWidget(email_label)

        email_value = QLabel("support@freegamehub.com")
        email_value.setStyleSheet("color: #4a9eff; font-size: 14px;")
        contacts_layout.addWidget(email_value)

        layout.addWidget(contacts_widget)
        layout.addStretch()

        # Кнопка закрытия
        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(dialog.accept)
        close_btn.setAlignment(Qt.AlignCenter)
        layout.addWidget(close_btn)

        dialog.exec_()