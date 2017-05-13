from PyQt5.QtWidgets import QMainWindow

from eview.view.pyqt.pyqt5.model.qwidget.qwidget import Qwidget


class Qmainwindow(QMainWindow, Qwidget):
    def __init__(self, *args, **kwargs):
        super(Qmainwindow, self).__init__(*args, **kwargs)
