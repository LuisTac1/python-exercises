"""
Theoretical numeric register generator with GUI interface
"""
import sys
from validacpf import validates_num
from geradorcpf import generat_num
from PyQt5.QtWidgets import QApplication, QMainWindow
import desing
print(generat_num())

class GeraValidaCPF(QMainWindow, desing.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeneratNum.clicked.connect(self.generat_num)
        self.btnValidNum.clicked.connect(self.validates_num)

    def generat_num(self):
        self.labelReturn.setText(
            str(generat_num())
        )

    def validates_num(self):
        cpf = self.inputValidNum.text()
        self.labelReturn.setText(
            str(validates_num(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    generat_valid_num = GeraValidaCPF()
    generat_valid_num.show()
    qt.exec_()
