from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

class LibraryTab(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.library_games = []
        self.empty_label = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        # Заголовок
        title = QLabel("📚 Моя библиотека")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #ffffff; margin-bottom: 10px;")
        layout.addWidget(title)

        # Статистика
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
                    QFrame {
                        background-color: #3a3a3a;
                        border: 1px solid #5a5a5a;
                        border-radius: 8px;
                    }
                """)

        stats_layout = QHBoxLayout(stats_frame)
        stats_layout.setContentsMargins(20, 15, 20, 15)

        stats = [
            ("0", "Игр"),
            ("0 GB", "Места"),
            ("0 ч", "Время")
        ]

        for value, label_text in stats:
            stat_widget = QWidget()
            stat_layout = QVBoxLayout(stat_widget)
            stat_layout.setAlignment(Qt.AlignCenter)

            value_label = QLabel(value)
            value_label.setStyleSheet("color: #4a9eff; font-size: 18px; font-weight: bold;")

            label = QLabel(label_text)
            label.setStyleSheet("color: #aaaaaa; font-size: 12px;")

            stat_layout.addWidget(value_label)
            stat_layout.addWidget(label)
            stats_layout.addWidget(stat_widget)

        layout.addWidget(stats_frame)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #5a5a5a; margin: 10px 0;")
        layout.addWidget(separator)

        # Список игр в библиотеке
        games_container = QWidget()
        games_container.setStyleSheet("""
                    QWidget {
                        background-color: #2a2a2a;
                        border-radius: 8px;
                        padding: 10px;
                    }
                """)

        games_layout = QVBoxLayout(games_container)
        games_layout.setSpacing(10)

        games_label = QLabel("Мои игры:")
        games_label.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold; padding: 5px;")
        games_layout.addWidget(games_label)

        # Контейнер для игр
        self.games_container = QWidget()
        self.games_layout = QVBoxLayout(self.games_container)
        self.games_layout.setSpacing(10)

        # Сообщение, если библиотека пуста
        self.empty_label = QLabel("Ваша библиотека пуста\nДобавьте игры из магазина!")
        self.empty_label.setStyleSheet("color: #888888; font-size: 14px; padding: 40px;")
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.games_layout.addWidget(self.empty_label)

        self.games_layout.addStretch()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.games_container)
        scroll.setStyleSheet("""
                    QScrollArea {
                        border: none;
                        background-color: transparent;
                    }
                """)

        games_layout.addWidget(scroll, 1)
        layout.addWidget(games_container, 1)

        self.setLayout(layout)

    def add_game(self, game):
        if game not in self.library_games:
            self.library_games.append(game)
            self.update_display()
            self.update_stats()

    def remove_game(self, game):
        if game in self.library_games:
            self.library_games.remove(game)
            self.update_display()
            self.update_stats()

    def update_display(self):
        # Удаляем все виджеты игр
        for i in reversed(range(self.games_layout.count())):
            widget = self.games_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if not self.library_games:
            # Показываем сообщение о пустой библиотеке
            self.empty_label = QLabel("Ваша библиотека пуста\nДобавьте игры из магазина!")
            self.empty_label.setStyleSheet("color: #888888; font-size: 14px; padding: 40px;")
            self.empty_label.setAlignment(Qt.AlignCenter)
            self.games_layout.addWidget(self.empty_label)
        else:
            # Скрываем сообщение о пустой библиотеке
            for i in range(self.games_layout.count()):
                widget = self.games_layout.itemAt(i).widget()
                if widget and widget == self.empty_label:
                    widget.hide()
                    break

            # Добавляем виджеты игр
            for game in self.library_games:
                game_widget = self.create_library_game_widget(game)
                self.games_layout.addWidget(game_widget)

        self.games_layout.addStretch()

    def create_library_game_widget(self, game):
        frame = QFrame()
        frame.setStyleSheet(f"""
                    QFrame {{
                        background-color: #3a3a3a;
                        border-left: 4px solid {game['color']};
                        border-radius: 6px;
                    }}
                """)

        layout = QHBoxLayout(frame)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        # Информация об игре
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setSpacing(5)

        name_label = QLabel(game["name"])
        name_label.setStyleSheet(f"color: {game['color']}; font-size: 16px; font-weight: bold;")
        info_layout.addWidget(name_label)

        details_label = QLabel(f"{game['genre']} • {game['size']}")
        details_label.setStyleSheet("color: #cccccc; font-size: 12px;")
        info_layout.addWidget(details_label)

        layout.addWidget(info_widget, 1)

        # Кнопки действий
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        buttons_layout.setSpacing(10)

        # Кнопка запуска
        play_btn = QPushButton("▶ Запустить")
        play_btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {game['color']};
                        color: #ffffff;
                        border: none;
                        border-radius: 4px;
                        padding: 8px 15px;
                        font-size: 13px;
                    }}
                    QPushButton:hover {{
                        background-color: {self.lighten_color(game['color'])};
                    }}
                """)
        play_btn.clicked.connect(lambda: self.launch_game(game))
        play_btn.setCursor(Qt.PointingHandCursor)
        buttons_layout.addWidget(play_btn)

        # Кнопка удаления
        remove_btn = QPushButton("🗑️ Удалить")
        remove_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #ff6b6b;
                        color: #ffffff;
                        border: none;
                        border-radius: 4px;
                        padding: 8px 15px;
                        font-size: 13px;
                    }
                    QPushButton:hover {
                        background-color: #ff8a8a;
                    }
                """)
        remove_btn.clicked.connect(lambda: self.remove_game(game))
        remove_btn.setCursor(Qt.PointingHandCursor)
        buttons_layout.addWidget(remove_btn)

        layout.addWidget(buttons_widget)

        return frame

    def lighten_color(self, color):
        if color.startswith("#"):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            r = min(255, int(r * 1.2))
            g = min(255, int(g * 1.2))
            b = min(255, int(b * 1.2))
            return f"#{r:02x}{g:02x}{b:02x}"
        return color

    def launch_game(self, game):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Запуск игры '{game['name']}'...\n\nИгра запускается в отдельном окне.")
        msg.setWindowTitle("Запуск игры")
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

    def update_stats(self):
        total_games = len(self.library_games)

        # Вычисляем общий размер
        total_size = 0
        for game in self.library_games:
            size_str = game["size"]
            if "GB" in size_str:
                size = float(size_str.replace("GB", "").strip())
                total_size += size
            elif "MB" in size_str:
                size = float(size_str.replace("MB", "").strip()) / 1024
                total_size += size

        # Обновляем статистику
        stats_widget = self.findChild(QFrame)
        if stats_widget:
            labels = stats_widget.findChildren(QLabel)
            if len(labels) >= 3:
                labels[0].setText(str(total_games))
                labels[1].setText(f"{total_size:.1f} GB")
                # Обновляем время (просто пример, можно добавить логику отслеживания времени)
                labels[2].setText(f"{total_games * 10} ч")