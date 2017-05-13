from PyQt5.QtCore import QObject

from eview.view.pyqt.pyqt5.model.model import Model


class Qobject(QObject, Model):
    def __init__(self, *args, **kwargs):
        super(Qobject, self).__init__(*args, **kwargs)

    def eventFilter(self, qobject, qevent):
        return super(Qobject, self).eventFilter(qobject, qevent)

