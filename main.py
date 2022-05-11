import random
import binascii
from rsa_cipher import RSA
from sha_hash import sha
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_mainwindow import Ui_MainWindow


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.from_data = None
        self.to_data = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.save.triggered.connect(self.save)
        self.ui.open.triggered.connect(self.open)
        self.ui.btn_main.clicked.connect(lambda: self.generate())
        self.ui.btn_encrypt.clicked.connect(lambda: self.encrypt())
        self.ui.btn_decrypt.clicked.connect(lambda: self.decrypt())
        self.ui.btn_clear.clicked.connect(lambda: self.clear())

    def generate(self, length=256):
        if not self.ui.main_line_p.text():
            p = RSA.get_prime(length)
            self.ui.main_line_p.setText(str(p))
        elif not RSA.is_prime(int(self.ui.main_line_p.text())):
            QMessageBox.information(self, "Error", "P is not Prime!", QMessageBox.Ok)
            return
        if not self.ui.main_line_q.text():
            q = RSA.get_prime(length)
            self.ui.main_line_q.setText(str(q))
        elif not RSA.is_prime(int(self.ui.main_line_q.text())):
            QMessageBox.information(self, "Error", "Q is not Prime!", QMessageBox.Ok)
            return
        p = int(self.ui.main_line_p.text())
        q = int(self.ui.main_line_q.text())
        if p == q:
            QMessageBox.information(self, "Error", "P & Q must be different!", QMessageBox.Ok)
            return
        N = p * q
        phiN = (p - 1) * (q - 1)
        if not self.ui.main_line_public.text():
            while True:
                public_key = RSA.get_prime(length - 1)
                if RSA.gcd(public_key, phiN) == 1:
                    break
            self.ui.main_line_public.setText(str(public_key))
        elif not RSA.is_prime(int(self.ui.main_line_public.text())):
            QMessageBox.information(self, "Error", "Public Key is not Prime!", QMessageBox.Ok)
            return
        elif RSA.gcd(int(self.ui.main_line_public.text()), phiN) != 1:
            QMessageBox.information(self, "Error", "Public Key & phi(N) is not relatively prime!", QMessageBox.Ok)
            return
        else:
            public_key = int(self.ui.main_line_public.text())
        self.ui.main_line_N.setText(str(N))
        self.ui.main_line_phi.setText(str(phiN))
        private_key = pow(public_key, -1, phiN)
        self.ui.main_line_private.setText(str(private_key))

    def encrypt(self):
        N, public_key = None, None

        if self.ui.main_line_N.text():
            N = int(self.ui.main_line_N.text())
        if N < 256:
            QMessageBox.information(self, "Error", "The alphabe length must be smaller or equal N", QMessageBox.Ok)
            return
        if not self.ui.from_line_N.text():
            if self.ui.main_line_N.text():
                self.ui.from_line_N.setText(self.ui.main_line_N.text())
        if self.ui.from_line_N.text():
            N = int(self.ui.from_line_N.text())

        if not self.ui.from_line_public.text():
            if self.ui.main_line_public.text():
                self.ui.from_line_public.setText(self.ui.main_line_public.text())
        if self.ui.from_line_public.text():
            public_key = int(self.ui.from_line_public.text())

        text = self.ui.from_text.toPlainText()
        encoded = RSA.encrypt(public_key, N, text)
        self.ui.to_text.setText(encoded)

    def decrypt(self):
        N, private_key = None, None
        if not self.ui.to_line_N.text():
            if self.ui.main_line_N.text():
                self.ui.to_line_N.setText(self.ui.main_line_N.text())
        if self.ui.to_line_N.text():
            N = int(self.ui.to_line_N.text())
        if not self.ui.to_line_private.text():
            if self.ui.main_line_public.text():
                self.ui.to_line_private.setText(self.ui.main_line_private.text())
        if self.ui.to_line_private.text():
            private_key = int(self.ui.to_line_private.text())
        text = self.ui.from_text.toPlainText()
        decoded = RSA.decrypt(private_key, N, text)
        self.ui.to_text.setText(decoded)

    def clear(self):
        self.ui.main_line_p.clear()
        self.ui.main_line_q.clear()
        self.ui.main_line_N.clear()
        self.ui.main_line_phi.clear()
        self.ui.main_line_public.clear()
        self.ui.main_line_private.clear()
        self.ui.from_line_N.clear()
        self.ui.from_line_public.clear()
        self.ui.to_line_N.clear()
        self.ui.to_line_private.clear()
        self.ui.from_text.clear()
        self.ui.to_text.clear()
        self.to_data = None
        self.from_data = None

    def save(self):
        byte = b""
        file_name = QFileDialog.getSaveFileName(self, "Save File", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "wb") as file:
                try:
                    for i in self.ui.to_text.toPlainText().split():
                        byte += int(i).to_bytes(1, byteorder='little')
                    file.write(byte)
                except:
                    for i in self.ui.to_text.toPlainText().split():
                        byte += i.encode()
                    file.write(byte)

        else:
            QMessageBox.information(self, "Error", "No file name specified", QMessageBox.Ok)

    def open(self):
        byte = ""
        file_name = QFileDialog.getOpenFileName(self, "Open File", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "rb") as file:
                self.from_data = file.read()
                # self.ui.from_text.setText(str(self.from_data)[2:-1])
                for i in self.from_data:
                    i.to_bytes(1, byteorder='little')
                    byte += f"{i} "
                self.ui.from_text.setText(byte)
        else:
            QMessageBox.information(self, "Error", "No file name specified", QMessageBox.Ok)


def main():
    app = QApplication()
    window = GUI()
    app.exec()


if __name__ == "__main__":
    main()
