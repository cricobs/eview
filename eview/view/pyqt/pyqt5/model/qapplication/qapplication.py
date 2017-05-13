from PyQt5.QtWidgets import QApplication

from eview.view.pyqt.pyqt5.model.qobject.qobject import Qobject


class Qapplication(QApplication, Qobject):
    def __init__(self, *args, **kwargs):
        super(Qapplication, self).__init__(*args, **kwargs)

