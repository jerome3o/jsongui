from PyQt5.QtWidgets import QComboBox
from jsongui.core import BaseWidget


class EnumWidget(BaseWidget):
    def build(self):
        self.content_widget = QComboBox()
        self.content_widget.addItems(map(str, self.items))

        self.content_widget.currentTextChanged.connect(self.validate)
        self.layout.addWidget(self.content_widget)

    def get_validation_state(self):
        return 2

    @property
    def items(self):
        return self.schema.get("enum", [])

    def set_value(self, value):
        if value not in self.items:
            raise ValueError(
                f"Invalid enum option {value}, accepted value: {self.items}"
            )

        self.content_widget.setCurrentIndex(self.items.index(value))

    def get_value(self):
        value = {str(i): i for i in self.items}.get(
            [self.content_widget.currentText()], None
        )

        if value is None:
            ValueError(f"Something has gone wrong with the combobox {self.schema}")

        return value
