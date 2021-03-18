from pathlib import Path
from PyQt5.QtWidgets import QFileDialog


src_dir = Path(__file__).parent
root_dir = src_dir.parent


def get_validation_style(validation_state):
    styles_dir = src_dir / 'styles'

    if validation_state == 0:
        return open(styles_dir / "invalid.css").read()
    if validation_state == 1:
        return open(styles_dir / "almost_valid.css").read()
    if validation_state == 2:
        return open(styles_dir / "valid.css").read()

    raise ValueError(f"Invalid validation state: {validation_state}")

def open_file():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()", 
            "",
            "All Files (*);;Python Files (*.py)", 
            options=options
        )
        return fileName