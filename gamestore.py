from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from utils.constants import GAMES_DATA

class GameStoreTab(QWidget):
    def __init__(self, library_callback):
        super().__init__()
        self.library_callback = library_callback
        self.games = GAMES_DATA
        self.init_ui()

        self.library_callback = library_callback
        self.games = self.get_games_data()
        self.search_input = None
        self.scroll_area = None
        self.games_container = None
        self.games_layout = None
        self.genre_filter = None
        self.init_ui()

    def get_games_data(self):
        return [
            {
                "name": "Minecraft",
                "size": "2.1 GB",
                "genre": "Песочница",
                "rating": "4.9",
                "color": "#6bcc78",
                "price": "Бесплатно",
                "description": "Игра в жанре песочницы с открытым миром, где вы можете строить, исследовать и выживать. Создавайте уникальные миры, сражайтесь с монстрами и творите без ограничений.",
                "in_library": False
            },
            {
                "name": "Among Us",
                "size": "250 MB",
                "genre": "Социальная игра",
                "rating": "4.5",
                "color": "#ff6b6b",
                "price": "Бесплатно",
                "description": "Командная игра на социальную дедукцию. Игроки делятся на экипаж и самозванцев. Экипаж должен выполнять задания, а самозванцы — саботировать и устранять членов экипажа.",
                "in_library": False
            },
            {
                "name": "Fortnite",
                "size": "31 GB",
                "genre": "Баттл-рояль",
                "rating": "4.7",
                "color": "#ffb74d",
                "price": "Бесплатно",
                "description": "Бесплатная игра в жанре королевской битвы, известная своим ярким стилем, строительством и регулярными обновлениями с новым контентом и событиями.",
                "in_library": False
            },
            {
                "name": "Dota 2",
                "size": "15 GB",
                "genre": "MOBA",
                "rating": "4.8",
                "color": "#4a9eff",
                "price": "Бесплатно",
                "description": "Комплексная многопользовательская онлайн-битва на арене. Собирайте команду из героев с уникальными способностями и сражайтесь за уничтожение вражеской крепости.",
                "in_library": False
            },
            {
                "name": "CS:GO",
                "size": "20 GB",
                "genre": "Шутер",
                "rating": "4.6",
                "color": "#ff9800",
                "price": "Бесплатно",
                "description": "Тактический шутер от первого лица. Сражайтесь в командах террористов и контр-террористов в различных режимах игры на тщательно сбалансированных картах.",
                "in_library": False
            },
            {
                "name": "Valorant",
                "size": "18 GB",
                "genre": "Тактический шутер",
                "rating": "4.4",
                "color": "#ff5252",
                "price": "Бесплатно",
                "description": "Бесплатный тактический шутер от первого лица. Соревнуйтесь в командах по 5 человек, используя уникальные способности агентов и точную стрельбу.",
                "in_library": False
            },
            {
                "name": "Stardew Valley",
                "size": "500 MB",
                "genre": "Симулятор фермы",
                "rating": "4.9",
                "color": "#4caf50",
                "price": "Бесплатно",
                "description": "Расслабляющая игра о жизни в деревне. Управляйте своей фермой, выращивайте культуры, разводите животных, общайтесь с жителями и исследуйте пещеры.",
                "in_library": False
            },
            {
                "name": "Team Fortress 2",
                "size": "15 GB",
                "genre": "Шутер",
                "rating": "4.7",
                "color": "#e91e63",
                "price": "Бесплатно",
                "description": "Бесплатный мультиплеерный шутер с уникальными классами персонажей. Командные сражения с юмористическим стилем и разнообразным геймплеем.",
                "in_library": False
            },
            {
                "name": "Warframe",
                "size": "35 GB",
                "genre": "Экшен",
                "rating": "4.8",
                "color": "#03a9f4",
                "price": "Бесплатно",
                "description": "Кооперативный экшен в научно-фантастическом сеттинге. Играйте за Тенно, древних воинов, сражающихся в космических битвах.",
                "in_library": False
            },
            {
                "name": "Path of Exile",
                "size": "25 GB",
                "genre": "RPG",
                "rating": "4.7",
                "color": "#9c27b0",
                "price": "Бесплатно",
                "description": "Бесплатная ролевая игра с глубокой системой прокачки и большим количеством контента. Темное фэнтези с множеством возможностей для кастомизации.",
                "in_library": False
            }
        ]

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        # Заголовок и поиск
        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)

        title = QLabel("🛒 Магазин игр")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #ffffff; margin-bottom: 10px;")
        header_layout.addWidget(title)

        # Поиск и фильтры
        search_container = QWidget()
        search_layout = QHBoxLayout(search_container)

        # Улучшенная поисковая строка
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Поиск по названию или жанру...")
        self.search_input.setStyleSheet("""
                    QLineEdit {
                        background-color: #4a4a4a;
                        color: white;
                        border: 2px solid #4a9eff;
                        border-radius: 8px;
                        padding: 12px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                    QLineEdit:focus {
                        border-color: #5aaaff;
                        background-color: #555555;
                    }
                """)
        self.search_input.textChanged.connect(self.filter_games)
        search_layout.addWidget(self.search_input, 3)  # Растягиваем поиск

        # Фильтр по жанру
        self.genre_filter = QComboBox()
        self.genre_filter.addItem("Все жанры")
        genres = sorted(set(game["genre"] for game in self.games))
        self.genre_filter.addItems(genres)
        self.genre_filter.setStyleSheet("""
                    QComboBox {
                        background-color: #444444;
                        color: #ffffff;
                        border: 1px solid #5a5a5a;
                        border-radius: 6px;
                        padding: 10px;
                        min-width: 150px;
                    }
                    QComboBox:hover {
                        background-color: #555555;
                    }
                    QComboBox::drop-down {
                        border: none;
                    }
                """)
        self.genre_filter.currentTextChanged.connect(self.filter_games)
        search_layout.addWidget(self.genre_filter, 1)

        header_layout.addWidget(search_container)
        layout.addWidget(header_widget)

        # Список игр
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
                    QScrollArea {
                        border: none;
                        background-color: transparent;
                    }
                    QScrollBar:vertical {
                        background-color: #3a3a3a;
                        width: 10px;
                        border-radius: 5px;
                    }
                    QScrollBar::handle:vertical {
                        background-color: #5a5a5a;
                        border-radius: 5px;
                        min-height: 20px;
                    }
                """)

        self.games_container = QWidget()
        self.games_layout = QVBoxLayout(self.games_container)
        self.games_layout.setSpacing(10)

        self.display_games(self.games)

        self.scroll_area.setWidget(self.games_container)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)

    def display_games(self, games):
        # Очищаем предыдущие игры
        for i in reversed(range(self.games_layout.count())):
            widget = self.games_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if not games:
            no_results = QLabel("Игры не найдены")
            no_results.setStyleSheet("color: #888888; font-size: 14px; padding: 20px;")
            no_results.setAlignment(Qt.AlignCenter)
            self.games_layout.addWidget(no_results)
            return

        for game in games:
            game_widget = self.create_game_widget(game)
            self.games_layout.addWidget(game_widget)

        self.games_layout.addStretch()

    def create_game_widget(self, game):
        frame = QFrame()
        frame.setStyleSheet(f"""
                    QFrame {{
                        background-color: #3a3a3a;
                        border-left: 4px solid {game['color']};
                        border-radius: 6px;
                    }}
                """)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Верхняя строка: название и рейтинг
        top_row = QWidget()
        top_layout = QHBoxLayout(top_row)

        name_label = QLabel(game["name"])
        name_label.setStyleSheet(f"color: {game['color']}; font-size: 16px; font-weight: bold;")
        top_layout.addWidget(name_label)

        rating_widget = QWidget()
        rating_layout = QHBoxLayout(rating_widget)
        rating_layout.setSpacing(5)

        rating_icon = QLabel("★")
        rating_icon.setStyleSheet("color: #ffb74d; font-size: 14px;")
        rating_layout.addWidget(rating_icon)

        rating_label = QLabel(game["rating"])
        rating_label.setStyleSheet("color: #ffffff; font-weight: bold;")
        rating_layout.addWidget(rating_label)

        top_layout.addWidget(rating_widget)
        layout.addWidget(top_row)

        # Вторая строка: жанр и размер
        details_row = QWidget()
        details_layout = QHBoxLayout(details_row)

        genre_label = QLabel(game["genre"])
        genre_label.setStyleSheet("color: #cccccc; font-size: 12px;")
        details_layout.addWidget(genre_label)

        size_label = QLabel(f"📦 {game['size']}")
        size_label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        details_layout.addWidget(size_label)

        price_label = QLabel(game["price"])
        price_label.setStyleSheet("color: #6bcc78; font-weight: bold; font-size: 12px;")
        details_layout.addWidget(price_label)

        details_layout.addStretch()
        layout.addWidget(details_row)

        # Кнопки
        buttons_row = QWidget()
        buttons_layout = QHBoxLayout(buttons_row)
        buttons_layout.setSpacing(10)

        # Кнопка "Об игре"
        info_btn = QPushButton("📖 Об игре")
        info_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #5a5a5a;
                        color: #ffffff;
                        border: none;
                        border-radius: 4px;
                        padding: 8px 15px;
                        font-size: 13px;
                    }
                    QPushButton:hover {
                        background-color: #6a6a6a;
                    }
                """)
        info_btn.clicked.connect(lambda: self.show_game_info(game))
        info_btn.setCursor(Qt.PointingHandCursor)
        buttons_layout.addWidget(info_btn)

        # Кнопка добавления/удаления из библиотеки
        if game["in_library"]:
            lib_btn = QPushButton("🗑️ Удалить из библиотеки")
            lib_btn.setStyleSheet("""
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
            lib_btn.clicked.connect(lambda: self.remove_from_library(game))
        else:
            lib_btn = QPushButton("📥 Добавить в библиотеку")
            lib_btn.setStyleSheet(f"""
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
            lib_btn.clicked.connect(lambda: self.add_to_library(game))

        lib_btn.setCursor(Qt.PointingHandCursor)
        buttons_layout.addWidget(lib_btn)

        buttons_layout.addStretch()
        layout.addWidget(buttons_row)

        return frame

    def lighten_color(self, color):
        # Простая функция для осветления цвета
        if color.startswith("#"):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            r = min(255, int(r * 1.2))
            g = min(255, int(g * 1.2))
            b = min(255, int(b * 1.2))
            return f"#{r:02x}{g:02x}{b:02x}"
        return color

    def show_game_info(self, game):
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Об игре: {game['name']}")
        dialog.setFixedSize(500, 400)
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

        # Заголовок
        title_label = QLabel(game["name"])
        title_label.setStyleSheet(f"color: {game['color']}; font-size: 20px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Информация о игре
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setSpacing(10)

        # Жанр, размер, цена
        details_widget = QWidget()
        details_layout = QHBoxLayout(details_widget)

        for label, value in [("🎮 Жанр", game["genre"]),
                             ("📦 Размер", game["size"]),
                             ("💰 Цена", game["price"]),
                             ("⭐ Рейтинг", game["rating"])]:
            detail_widget = QWidget()
            detail_layout = QVBoxLayout(detail_widget)
            detail_layout.setSpacing(5)

            detail_label = QLabel(label)
            detail_label.setStyleSheet("color: #aaaaaa; font-size: 11px;")
            detail_layout.addWidget(detail_label)

            value_label = QLabel(value)
            value_label.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 12px;")
            detail_layout.addWidget(value_label)

            details_layout.addWidget(detail_widget)

        info_layout.addWidget(details_widget)

        # Описание
        desc_label = QLabel("📝 Описание:")
        desc_label.setStyleSheet("color: #ffffff; font-weight: bold; margin-top: 10px;")
        info_layout.addWidget(desc_label)

        desc_text = QLabel(game["description"])
        desc_text.setWordWrap(True)
        desc_text.setStyleSheet("color: #cccccc; font-size: 13px; line-height: 1.4;")
        desc_text.setAlignment(Qt.AlignLeft)
        info_layout.addWidget(desc_text)

        layout.addWidget(info_widget)

        # Кнопки
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(dialog.accept)
        buttons_layout.addWidget(close_btn)

        if not game["in_library"]:
            add_btn = QPushButton("Добавить в библиотеку")
            add_btn.setStyleSheet(f"background-color: {game['color']};")
            add_btn.clicked.connect(lambda: (self.add_to_library(game), dialog.accept()))
            buttons_layout.addWidget(add_btn)

        layout.addWidget(buttons_widget)

        dialog.exec_()

    def add_to_library(self, game):
        game["in_library"] = True
        self.library_callback(game, True)

        # Обновляем отображение
        self.filter_games()

        # Показываем уведомление
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Игра '{game['name']}' добавлена в вашу библиотеку!")
        msg.setWindowTitle("Успешно")
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

    def remove_from_library(self, game):
        game["in_library"] = False
        self.library_callback(game, False)

        # Обновляем отображение
        self.filter_games()

        # Показываем уведомление
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Игра '{game['name']}' удалена из вашей библиотеки.")
        msg.setWindowTitle("Успешно")
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

    def filter_games(self):
        search_text = self.search_input.text().lower()
        selected_genre = self.genre_filter.currentText()

        filtered_games = []

        for game in self.games:
            matches_search = (search_text in game["name"].lower() or
                              search_text in game["genre"].lower() or
                              search_text in game["description"].lower())

            matches_genre = (selected_genre == "Все жанры" or
                             game["genre"] == selected_genre)

            if matches_search and matches_genre:
                filtered_games.append(game)

        self.display_games(filtered_games)