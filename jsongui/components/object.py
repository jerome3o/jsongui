from typing import List
from PyQt5.QtWidgets import QComboBox, QVBoxLayout
from jsongui.core import BaseWidget


class ObjectWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.property_widgets: List[BaseWidget] = []

    def build(self):
        self.content = QVBoxLayout()
        self.layout.addLayout(self.content)

    def get_validation_state(self):
        return min([
            p.get_validation_state() for p in self.property_widgets
        ])

    def add_property(self, property: BaseWidget):
        self.property_widgets.append(property)
        self.content.addWidget(property)

    def set_value(self, value):
        raise NotImplemented()

    def get_value(self):
        return {
            p.title: p.get_value()
            for p in self.property_widgets
        }
