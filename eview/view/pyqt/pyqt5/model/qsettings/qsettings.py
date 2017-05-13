import logging

from PyQt5.QtCore import QSettings

from eview.model.path.pathFind import PathFind
from eview.view.pyqt.pyqt5.model.qevent.qevent import QeventSettingsRestore, QeventSettingsSave
from eview.view.pyqt.pyqt5.model.qobject.qobject import Qobject


class Qsettings(QSettings, Qobject):
    def __init__(self, *args, **kwargs):
        super(Qsettings, self).__init__(*args, **kwargs)


class QsettingsRelative(Qsettings, PathFind):
    def __init__(self, parent, *args, **kwargs):
        filename = self.relative(parent, extension="ini")

        super(QsettingsRelative, self).__init__(filename, self.IniFormat, parent, *args, **kwargs)


def qobject_names(qobject):
    return filter(lambda x: x.startswith("setting_"), dir(qobject))


class QsettingsProperty(Qsettings):
    def __init__(self, *args, **kwargs):
        super(QsettingsProperty, self).__init__(*args, **kwargs)

        self.parent().installEventFilter(self)

    def eventFilter(self, qobject, qevent):
        if qevent.type() == QeventSettingsRestore.qevent_type:
            self.restore(qobject)
            qevent.accept()
        elif qevent.type() == QeventSettingsSave.qevent_type:
            self.save(qobject)
            qevent.accept()

        return super(QsettingsProperty, self).eventFilter(qobject, qevent)

    def restore(self, qobject):
        self.beginGroup(qobject.__class__.__name__)
        for name in qobject_names(qobject):
            try:
                setattr(qobject, name, self.value(name))
            except TypeError:
                logging.warning("restore: {0} failed".format(name))

        self.endGroup()

    def save(self, qobject):
        self.beginGroup(qobject.__class__.__name__)
        for name in qobject_names(qobject):
            self.setValue(name, getattr(qobject, name))

        self.endGroup()
