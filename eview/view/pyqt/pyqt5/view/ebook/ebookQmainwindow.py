from eview.view.pyqt.pyqt5.model.qmainwindow.qmainwindow import Qmainwindow
from eview.view.pyqt.pyqt5.view.ebook.ebook import Ebook


class EbookQmainwindow(Qmainwindow, Ebook):
    setting_geometry = property(Qmainwindow.saveGeometry, Qmainwindow.restoreGeometry)
    setting_state = property(Qmainwindow.saveState, Qmainwindow.restoreState)

    def __init__(self, *args, **kwargs):
        super(EbookQmainwindow, self).__init__(*args, **kwargs)
