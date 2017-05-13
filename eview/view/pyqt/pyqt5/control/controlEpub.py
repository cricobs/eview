import sys

from eview.view.pyqt.pyqt5.control.control import Control
from eview.view.pyqt.pyqt5.view.ebook.ebookQapplication import EbookQapplication
from eview.view.pyqt.pyqt5.view.ebook.ebookQmainwindow import EbookQmainwindow


class ControlEpub(Control):
    def __init__(self, *args, **kwargs):
        super(ControlEpub, self).__init__(*args, **kwargs)

        self.qapplication = EbookQapplication(sys.argv)

        self.qmainwindow = EbookQmainwindow()
        self.qmainwindow.show()

        sys.exit(self.qapplication.exec_())
