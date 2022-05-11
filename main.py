import pickle
from rsa_cipher import RSA
from sha_hash import sha
from PySide6.QtWidgets import *
from ui_mainwindow import Ui_MainWindow


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.from_data = None
        self.to_data = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.open.triggered.connect(self.open)
        self.ui.sign_save.triggered.connect(self.save_sign)
        self.ui.sign_load.triggered.connect(self.load_sign)
        self.ui.btn_main.clicked.connect(lambda: self.generate())
        self.ui.btn_encrypt.clicked.connect(lambda: self.sign())
        self.ui.btn_decrypt.clicked.connect(lambda: self.verify())
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
        if N.bit_length() < 160:
            QMessageBox.information(self, "Error", f"Bit length of N must be more than 160!\nCurrent length: {N.bit_length()}", QMessageBox.Ok)
            return
        self.ui.main_line_phi.setText(str(phiN))
        private_key = pow(public_key, -1, phiN)
        self.ui.main_line_private.setText(str(private_key))

    def sign(self):
        N, private_key = None, None
        if self.ui.main_line_N.text():
            N = int(self.ui.main_line_N.text())
        if not self.ui.from_line_N.text():
            if self.ui.main_line_N.text():
                self.ui.from_line_N.setText(self.ui.main_line_N.text())
        if self.ui.from_line_N.text():
            N = int(self.ui.from_line_N.text())
        if not self.ui.from_line_private.text():
            if self.ui.main_line_private.text():
                self.ui.from_line_private.setText(self.ui.main_line_private.text())
        if self.ui.from_line_private.text():
            private_key = int(self.ui.from_line_private.text())
        text = self.ui.text.toPlainText()
        message_hash = sha(text)
        sign = pow(int(message_hash, 16), private_key, N)
        self.ui.from_sign.setText(f"{sign:x}")

    def verify(self):
        N, public_key = None, None
        self.ui.to_hash.clear()
        self.ui.to_hash_actual.clear()
        if not self.ui.to_line_N.text():
            if self.ui.main_line_N.text():
                self.ui.to_line_N.setText(self.ui.main_line_N.text())
        if self.ui.to_line_N.text():
            N = int(self.ui.to_line_N.text())
        if not self.ui.to_line_public.text():
            if self.ui.main_line_public.text():
                self.ui.to_line_public.setText(self.ui.main_line_public.text())
        if self.ui.to_line_public.text():
            public_key = int(self.ui.to_line_public.text())
        text = self.ui.text.toPlainText()
        decoded_hash = sha(text)
        self.ui.to_hash_actual.setText(decoded_hash)
        from_sign = self.ui.from_sign.text()
        sign = pow(int(from_sign, 16), public_key, N)
        self.ui.to_hash.setText(f"{sign:x}")
        if str(decoded_hash) == f"{sign:x}":
            QMessageBox.information(self, "Success", "Sign is correct", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Error", "Invalid sign!", QMessageBox.Ok)

    def clear(self):
        self.ui.main_line_p.clear()
        self.ui.main_line_q.clear()
        self.ui.main_line_N.clear()
        self.ui.main_line_phi.clear()
        self.ui.main_line_public.clear()
        self.ui.main_line_private.clear()
        self.ui.from_line_N.clear()
        self.ui.from_line_private.clear()
        self.ui.to_line_N.clear()
        self.ui.to_line_public.clear()
        self.ui.text.clear()
        self.ui.from_sign.clear()
        self.ui.to_hash.clear()
        self.ui.to_hash_actual.clear()
        self.to_data = None
        self.from_data = None

    def open(self):
        byte = ""
        file_name = QFileDialog.getOpenFileName(self, "Open File", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "rb") as file:
                self.from_data = file.read()
                for i in self.from_data:
                    i.to_bytes(1, byteorder='little')
                    byte += f"{i} "
                self.ui.text.setText(byte)
        else:
            QMessageBox.information(self, "Error", "No file name specified", QMessageBox.Ok)

    def save_sign(self):
        file_name = QFileDialog.getSaveFileName(self, "Save Sign", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "wb") as file:
                pickle.dump((self.ui.from_sign.text(), self.ui.main_line_public.text(), self.ui.main_line_N.text(), self.ui.text.toPlainText()), file)
        else:
            QMessageBox.information(self, "Error", "No file name specified", QMessageBox.Ok)

    def load_sign(self):
        file_name = QFileDialog.getOpenFileName(self, "Open Sign", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "rb") as file:
                sign, public_key, N, message = pickle.load(file)
            self.ui.from_sign.setText(sign)
            self.ui.text.setText(message)
            self.ui.to_line_public.setText(public_key)
            self.ui.to_line_N.setText(N)
        else:
            QMessageBox.information(self, "Error", "No file name specified", QMessageBox.Ok)


def main():
    app = QApplication()
    window = GUI()
    app.exec()


if __name__ == "__main__":
    main()
