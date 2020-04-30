from PyQt5 import QtCore, QtGui, QtWidgets
from guitemplate import Ui_Form

class TemptForm(Ui_Form):
    def __init__(self):
        super(TemptForm, self).__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.f_convert)
        self.pushButton_2.clicked.connect(self.c_convert)
        self.lineEdit.setText("32.0")
        self.lineEdit_2.setText("0.0")
        self.lineEdit.returnPressed.connect(self.f_convert)
        self.lineEdit_2.returnPressed.connect(self.c_convert)

    def f_convert(self):
            words = self.lineEdit.text()
            try:
                ftemp = float(words)
            except (ValueError, TypeError):
                self.lineEdit_2.setText('')
                return
            self.lineEdit_2.setText('%.1f' % self.f_to_c(ftemp))
            return

    def c_convert(self):
        words = self.lineEdit_2.text()
        try:
            ctemp = float(words)
        except (ValueError, TypeError):
            self.lineEdit.setText('')
            return
        self.lineEdit.setText('%.1f' % self.c_to_f(ctemp))
        return

    def f_to_c(self, temp):
        return (temp - 32) * 5 / 9

    def c_to_f(self, temp):
        return temp * 9 / 5 + 32


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = TemptForm()
    main.show()
    sys.exit(app.exec_())
    return 0

if __name__ == '__main__':
    main()


