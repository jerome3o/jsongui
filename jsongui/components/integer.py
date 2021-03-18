from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIntValidator

from jsongui.core import BaseWidget

class IntegerWidget(BaseWidget):
    def build(self):
        self.content_widget = QLineEdit()
        self.content_widget.textChanged.connect(self.validate)
        self.layout.addWidget(self.content_widget)

    def get_validation_state(self):
        text = self.content_widget.text()
        return QIntValidator().validate(text, 7)[0]

    def get_value(self):
        return int(self.content_widget.text())

    def set_value(self, value):
        return self.content_widget.setText(str(value))