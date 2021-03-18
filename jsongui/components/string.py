from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton

from jsongui.core import BaseWidget
from jsongui.helpers import open_file

class StringWidget(BaseWidget):
    def build(self):
        self.content_widget = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.content_widget)

        if self.title.endswith("path"):

            def callback():
                file = open_file()
                if file:
                    self.content_widget.setText(file)

            button = QPushButton()
            button.clicked.connect(callback)
            button.setText("...")
            layout.addWidget(button)

        self.layout.addLayout(layout)

    def get_value(self):
        return self.content_widget.toPlainText()

    def set_value(self, value):
        return self.content_widget.setText(value)