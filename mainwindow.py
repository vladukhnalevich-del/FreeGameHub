import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from modules.gamestore import GameStoreTab
from modules.library import LibraryTab
from modules.profile import ProfileTab


class FreeGameHub(QMainWindow):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.setWindowTitle(f"FreeGameHub | {user_data['login']}")
        self.setGeometry(100, 100, 1100, 750)
        self.library_tab = None

        # Вызываем методы инициализации
        self.setup_styles()  # Теперь этот метод существует
        self.init_ui()

    def setup_styles(self):
        """Настройка стилей главного окна"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2c2c;
            }
            QTabWidget::pane {
                border: 1px solid #444444;
                border-radius: 8px;
                background-color: #3a3a3a;
                top: -1px;
            }
            QTabBar::tab {
                background-color: #444444;
                color: #ffffff;
                padding: 15px 30px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                font-weight: bold;
                font-size: 14px;
                margin-right: 2px;
                min-width: 120px;
            }
            QTabBar::tab:selected {
                background-color: #4a9eff;
                color: #ffffff;
            }
            QTabBar::tab:hover {
                background-color: #555555;
            }
        """)

    def init_ui(self):
        """Инициализация пользовательского интерфейса"""
        # Центральный виджет с вкладками
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.setCentralWidget(self.tabs)

        # Добавляем вкладки
        self.library_tab = LibraryTab(self.user_data)
        self.tabs.addTab(GameStoreTab(self.update_library), "🛒 Магазин")
        self.tabs.addTab(self.library_tab, "📚 Библиотека")
        self.tabs.addTab(ProfileTab(self.user_data, self), "👤 Профиль")

        # Верхняя панель
        self.create_toolbar()

    def create_toolbar(self):
        """Создание верхней панели инструментов"""
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setStyleSheet("""
            QToolBar {
                background-color: #3a3a3a;
                border: none;
                padding: 8px;
                spacing: 10px;
            }
        """)
        self.addToolBar(toolbar)

        # Приветствие
        greeting = QLabel(f"🎮 Добро пожаловать, {self.user_data['name']}!")
        greeting.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 14px; padding: 0 15px;")
        toolbar.addWidget(greeting)

        toolbar.addSeparator()

        # ID пользователя
        id_label = QLabel(f"ID: {self.user_data['id']}")
        id_label.setStyleSheet("color: #aaaaaa; font-size: 12px; padding: 0 10px;")
        toolbar.addWidget(id_label)

        toolbar.addSeparator()

        # Кнопка обновления
        refresh_btn = QPushButton("🔄 Обновить")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        refresh_btn.setCursor(Qt.PointingHandCursor)
        toolbar.addWidget(refresh_btn)

        # Пустое пространство для выравнивания
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        # Кнопка выхода
        logout_btn = QPushButton("🚪 Выйти")
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff6b6b;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff8a8a;
            }
        """)
        logout_btn.clicked.connect(self.close)
        logout_btn.setCursor(Qt.PointingHandCursor)
        toolbar.addWidget(logout_btn)

    def update_library(self, game, add):
        """Обновление библиотеки игр"""
        if add:
            self.library_tab.add_game(game)
        else:
            self.library_tab.remove_game(game)