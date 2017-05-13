from eview.control.control import Control
from eview.view.pyqt.pyqt5.control.controlEpub import ControlEpub as CEpub


class ControlEpub(Control):
    def __init__(self, *args, **kwargs):
        super(ControlEpub, self).__init__(*args, **kwargs)

        self.control = CEpub()


if __name__ == "__main__":
    ControlEpub()
