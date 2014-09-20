import sys
from PyQt4 import QtCore, QtGui

class LaggyGui(QtGui.QWidget):
    STATE_IDLE = 0
    STATE_RECORDING = 1

    def __init__(self):
        super(LaggyGui, self).__init__()
        self.state = self.STATE_IDLE
        self.setWindowTitle('Laggy')

        # XXX: some day you will have an icon :)
        #self.setWindowIcon(window_icon)

        # message log
        self.message_log = QtGui.QListWidget()

        # record button
        self.button = QtGui.QPushButton('Record Message')
        self.button.clicked.connect(self.button_clicked)

        # main layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.message_log)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.show()

        self.log('Check it out, you can log messages')

    def button_clicked(self):
        self.log('The button was clicked')

        if self.state == self.STATE_IDLE:
            self.state = self.STATE_RECORDING
            self.button.setText('Stop Recording')
            # XXX: start recording
            self.log('Recording should start now')

        elif self.state == self.STATE_RECORDING:
            self.state = self.STATE_IDLE
            self.button.setText('Record Message')
            self.log('Recording should stop now')
            # XXX: stop recording

    def log(self, msg):
        item = QtGui.QListWidgetItem(msg)
        self.message_log.addItem(item)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = LaggyGui()
    sys.exit(app.exec_())
