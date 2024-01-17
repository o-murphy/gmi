"""
# QtMDI (Qt Material Design Icons)
qtawesome extension with the latest variable icon fonts for Material Symbols (Python 3)
(C) 2023 Yaroshenko Dmytro (https://github.com/o-murphy)
"""

import os
import sys
from enum import Enum

import qtawesome
from qtawesome.icon_browser import IconBrowser
from qtpy import QtWidgets

__author__ = "o-murphy"
__copyright__ = ("(C) 2023 Yaroshenko Dmytro (https://github.com/o-murphy)",)

__credits__ = ["o-murphy"]
# __version__ = "1.0.0"


SEARCH_DIR = os.path.dirname(__file__)
FONT_DIR = os.path.join(SEARCH_DIR, 'fonts')
SYMBOLS_DIR = os.path.join(SEARCH_DIR, 'icons')

_BUILT_IN_FONTS = (
    (
        "gmi",
        "MaterialIcons-Regular.ttf",
        "MaterialIcons-Regular-charmap.json",
    ),
    (
        "gmi-outlined",
        "MaterialIconsOutlined-Regular.otf",
        "MaterialIconsOutlined-Regular-charmap.json",
    ),
    (
        "gmi-round",
        "MaterialIconsRound-Regular.otf",
        "MaterialIconsRound-Regular-charmap.json",
    ),
    (
        "gmi-sharp",
        "MaterialIconsSharp-Regular.otf",
        "MaterialIconsSharp-Regular-charmap.json",
    ),
    (
        "gmi-2tone",
        "MaterialIconsTwoTone-Regular.otf",
        "MaterialIconsTwoTone-Regular-charmap.json",
    ),
)


def _create_symbols_prefix(filename):
    """creates prefix for dynamic loaded symbol fonts"""
    try:
        return f"gms-{os.path.splitext(filename)[0].split('-')[-1]}"
    # pylint: disable=broad-exception-caught
    except Exception as exc:
        print(exc)
        return "gms-other"


def _look_for_fonts():
    fonts = []
    for root, dirs, files in os.walk(SYMBOLS_DIR):
        path = root.split(os.sep)
        for file in files:
            if os.path.splitext(file)[1] == ".ttf":
                # filepath = os.path.join(root, file)
                prefix = f"{_create_symbols_prefix(file)}-{path[-1]}"
                fonts.append(
                    (prefix, file, "../charmap.json", root)
                )
    return fonts


def load(app: QtWidgets.QApplication):
    """loads fonts and symbols to current QApplication instance"""
    if app == QtWidgets.QApplication.instance():

        for symbols in _look_for_fonts():
            qtawesome.load_font(*symbols)

        for font in _BUILT_IN_FONTS:
            qtawesome.load_font(*font, FONT_DIR)


class Weight(Enum):
    w100 = 100
    w200 = 200
    w300 = 300
    w400 = 400
    w500 = 500
    w600 = 600
    w700 = 700


class Grade(Enum):
    low = -25
    mid = 0
    high = 200


class OpticalSize(Enum):
    o20 = 20
    o24 = 24
    o40 = 40
    o48 = 48


class Style(Enum):
    Outlined = 0
    Rounded = 1
    Sharp = 2


# def icon(name: str, fill: bool = False,
#          wght: Weight = Weight.w400,
#          grad: Grade = Grade.mid,
#          opsz: OpticalSize = OpticalSize.o24):


def icon(*names,
         # fill: bool = False,
         wght: Weight = Weight.w400,
         # grad: Grade = Grade.mid,
         # opsz: OpticalSize = OpticalSize.o24)
         **kwargs):
    return qtawesome.icon(*names, **kwargs)


def example():
    class W(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            self.lt = QtWidgets.QVBoxLayout(self)
            self.btn = QtWidgets.QToolButton(self)
            self.btn.setIcon(icon("gms-default.search"))
            self.lt.addWidget(self.btn)

    app = QtWidgets.QApplication()
    load(app)
    qtawesome.dark(app)
    w = W()
    w.show()
    sys.exit(app.exec_())


def run():
    """
    Start the IconBrowser and block until the process exits.
    """
    app = QtWidgets.QApplication()
    load(app)
    qtawesome.dark(app)

    browser = IconBrowser()
    browser.setWindowTitle('QtMDi Icon Browser')
    # pylint: disable=protected-access
    browser._comboFont.setCurrentText("gmi")
    browser.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
    # example()


