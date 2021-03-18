from typing import Callable, List
from PyQt5.QtWidgets import QAbstractItemView, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QWidget
from jsongui.core import BaseWidget


class ArrayWidget(BaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_widgets: List[BaseWidget] = []

        # needs to be set externally
        self.builder_function: Callable[[], BaseWidget] = lambda: None

    def build(self):
        self.content_widget = QListWidget()
        self.content_widget.setSelectionMode(QAbstractItemView.NoSelection)

        button_layout = QHBoxLayout()

        add_button = QPushButton("add")
        add_button.clicked.connect(self.add_new_item)

        button_layout.addWidget(add_button)
        button_layout.addStretch(0)

        self.layout.addWidget(self.content_widget)
        self.layout.addLayout(button_layout)

    def get_validation_state(self):
        return min([
            p.get_validation_state() for p in self.item_widgets
        ])

    def add_new_item(self):
        self.add_item(self.builder_function())

    def add_item(self, item: BaseWidget):
        self.item_widgets.append(item)

        # Create QListWidgetItem
        list_widget_item = QListWidgetItem()
        item_with_button = self.build_list_item(item)
        list_widget_item.setSizeHint(item_with_button.sizeHint())

        # Add QListWidgetItem into QListWidget
        self.content_widget.addItem(list_widget_item)
        self.content_widget.setItemWidget(list_widget_item, item_with_button)

    def build_list_item(self, item: BaseWidget):
        #TODO: This is nasty - it uses the index of item in item_widgets to remove the widget
        list_item = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(item)
        button = QPushButton()
        button.setText("remove")
        button.clicked.connect(lambda: self.remove_item(item))
        layout.addStretch(0)
        layout.addWidget(button)
        list_item.setLayout(layout)
        return list_item
    
    def remove_item(self, item: BaseWidget):
        index = self.item_widgets.index(item)
        self.content_widget.takeItem(index)
        self.item_widgets.pop(index)

    def set_value(self, value):
        raise NotImplemented()

    def get_value(self):
        return [
            p.get_value()
            for p in self.item_widgets
        ]
