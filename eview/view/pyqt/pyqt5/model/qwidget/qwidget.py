from PyQt5.QtWidgets import QWidget

from eview.view.pyqt.pyqt5.model.qevent.qevent import QeventUILoad, QeventSettingsSave, \
    QeventSettingsRestore
from eview.view.pyqt.pyqt5.model.qobject.qobject import Qobject


class Qwidget(QWidget, Qobject):
    def __init__(self, *args, **kwargs):
        super(Qwidget, self).__init__(*args, **kwargs)

        QeventUILoad(self)

    def event(self, qevent):
        if qevent.type() == QeventUILoad.qevent_type:
            qevent.accept()

        return super(Qwidget, self).event(qevent)

    def closeEvent(self, qcloseevent):
        QeventSettingsSave(self)
        super(Qwidget, self).closeEvent(qcloseevent)

    def showEvent(self, qshowevent):
        QeventSettingsRestore(self)
        super(Qwidget, self).showEvent(qshowevent)
