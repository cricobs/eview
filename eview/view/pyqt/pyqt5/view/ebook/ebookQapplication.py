from eview.view.pyqt.pyqt5.model.qapplication.qapplication import Qapplication
from eview.view.pyqt.pyqt5.view.ebook.ebook import Ebook
from eview.view.pyqt.pyqt5.view.ebook.ebookQsettings import EbookQsettings


class EbookQapplication(Qapplication, Ebook):
    def __init__(self, *args, **kwargs):
        super(EbookQapplication, self).__init__(*args, **kwargs)

        self.qsettings = EbookQsettings(self)
