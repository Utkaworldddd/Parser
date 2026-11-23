from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parser")
        self.resize(1200, 800)

        self.back_button = QPushButton("Назад")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Введите адрес сайта")
        self.open_button = QPushButton("Открыть")

        top = QHBoxLayout()
        top.addWidget(self.back_button)
        top.addWidget(self.url_input)
        top.addWidget(self.open_button)

        self.browser = QWebEngineView()

        layout = QVBoxLayout()
        layout.addLayout(top)
        layout.addWidget(self.browser)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        self.open_button.clicked.connect(self.open_url)
        self.url_input.returnPressed.connect(self.open_url)
        self.back_button.clicked.connect(self.browser.back)
        self.browser.urlChanged.connect(self.url_changed)

    def open_url(self):
        text = self.url_input.text().strip()
        if text == "":
            return
        if not text.startswith("http://") and not text.startswith("https://"):
            text = "https://" + text
        self.browser.setUrl(QUrl(text))

    def url_changed(self, url):
        self.url_input.setText(url.toString())
