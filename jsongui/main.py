from jsongui.components.array import ArrayWidget
from jsongui.components.object import ObjectWidget
from jsongui.components.enum import EnumWidget
from jsongui.components.number import NumberWidget
from jsongui.components.integer import IntegerWidget
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from jsongui.components.string import StringWidget


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    layout = QVBoxLayout()

    object_widget = ObjectWidget("hello?", {})

    object_widget.add_property(StringWidget("path item path", {"type": "string", "default": "hello"}))
    object_widget.add_property(StringWidget("string item", {"type": "string"}))
    object_widget.add_property(IntegerWidget("integer item", {"type": "integer"}))
    object_widget.add_property(NumberWidget("number item", {"type": "integer", "default": 4.3}))
    object_widget.add_property(EnumWidget("enum item", {'type': 'string', 'enum': ['value_1', 'value_2', 6]}))

    builder_function = lambda: EnumWidget("enum item", {'type': 'string', 'enum': ['value_1', 'value_2', 6]})

    array_widget = ArrayWidget("array item", {})
    array_widget.builder_function = builder_function

    layout.addWidget(array_widget)
    widget.setLayout(layout)

    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()