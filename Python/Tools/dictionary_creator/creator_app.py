import sys


from PySide2 import QtCore, QtGui, QtWidgets



























def main():
    app = QtWidgets.QApplication()
    box = QtWidgets.QMessageBox()
    box.setText("Hello World")
    box.exec()

    sys.exit(app.exec_())













if __name__ == '__main__':
    main()