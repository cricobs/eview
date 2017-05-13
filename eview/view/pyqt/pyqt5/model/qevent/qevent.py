from PyQt5.uic import loadUi

from PyQt5.QtCore import QEvent
from PyQt5.QtCore import pyqtWrapperType
from PyQt5.QtWidgets import QApplication

from eview.model.path.pathFind import PathFind
from eview.view.pyqt.pyqt5.model.model import Model


class pyqtwrappertype(pyqtWrapperType):
    _qevent_type = None

    @property
    def qevent_type(cls):
        if cls._qevent_type is None:
            cls._qevent_type = QEvent.registerEventType()

        return cls._qevent_type


class Qevent(QEvent, Model):
    __metaclass__ = pyqtwrappertype

    def __init__(self, *args, **kwargs):
        self._qevent_type = None

        try:
            super(Qevent, self).__init__(*args, **kwargs)
        except TypeError:
            super(Qevent, self).__init__(self.qevent_type, *args, **kwargs)
        else:
            self.qevent_type = self.type()

    @property
    def qevent_type(self):
        if self._qevent_type is None:
            self._qevent_type = self.__class__.qevent_type

        return self._qevent_type

    @qevent_type.setter
    def qevent_type(self, value):
        self._qevent_type = value


class QeventFile(Qevent, PathFind):
    pass


class QeventUILoaded(Qevent):
    pass


class QeventQwidget(Qevent):
    def __init__(self, qwidget, *args, **kwargs):
        super(QeventQwidget, self).__init__(*args, **kwargs)

        self.qwidget = qwidget

        QApplication.instance().sendEvent(qwidget, self)


class QeventUILoad(QeventQwidget, QeventFile):
    def accept(self):
        path = self.relative(self.qwidget, extension="ui")
        try:
            loadUi(path, self.qwidget)
        except IOError as e:
            if e.errno != 2:
                raise
        else:
            QApplication.instance().sendEvent(self.qwidget, QeventUILoaded())

            return True


class QeventSettings(QeventQwidget):
    pass


class QeventSettingsSave(QeventSettings):
    pass


class QeventSettingsRestore(QeventSettings):
    pass
