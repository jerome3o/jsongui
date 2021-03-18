from jsongui.helpers import get_validation_style
from typing import Dict, Union
from PyQt5.QtWidgets import QComboBox, QLineEdit, QWidget, QVBoxLayout, QLabel


class BaseWidget(QWidget):

    def __init__(
        self, 
        title: str,
        schema: Dict[str, Union[str, list, dict]]
    ):
        super().__init__()
        # TODO: add object and list type widgets here.
        self.content_widget: Union[QComboBox, QLineEdit] = None
        self.schema = schema
        self.title = title
        self.layout: QVBoxLayout = QVBoxLayout()
        self.layout.addWidget(
            QLabel(title)
        )
        self.build()

        self.setLayout(self.layout)
        default_value = schema.get("default")
        if default_value:
            self.set_value(default_value)
            self.validate()

    def build(self):
        raise NotImplemented()

    def get_value(self):
        raise NotImplemented()

    def set_value(self):
        raise NotImplemented()

    def get_validation_state(self) -> int:
        return 2

    def validate(self):
        validation_state = self.get_validation_state()
        self.setStyleSheet(get_validation_style(validation_state))