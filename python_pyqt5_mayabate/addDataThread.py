
from PyQt5 import QtCore


class addTableDataThread(QtCore.QThread):
    _signal = QtCore.pyqtSignal(dict)

    def __init__(self, data_dict, parent=None):
        super(addTableDataThread, self).__init__(parent)
        self.myForm = parent
        self.data_dict = data_dict

    def run(self):
        self.callback(self.data_dict)

    def callback(self, data_dict):
        self._signal.emit(data_dict)