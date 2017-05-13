from eview.view.pyqt.pyqt5.model.qsettings.qsettings import QsettingsRelative, QsettingsProperty


class EbookQsettings(QsettingsRelative, QsettingsProperty):
    def __init__(self, *args, **kwargs):
        super(EbookQsettings, self).__init__(*args, **kwargs)