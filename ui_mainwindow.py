# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 503)
        MainWindow.setMinimumSize(QSize(852, 503))
        self.open = QAction(MainWindow)
        self.open.setObjectName(u"open")
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        self.generate_key = QAction(MainWindow)
        self.generate_key.setObjectName(u"generate_key")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_4 = QFormLayout(self.centralwidget)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.main_prime_p = QLabel(self.centralwidget)
        self.main_prime_p.setObjectName(u"main_prime_p")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.main_prime_p)

        self.main_line_p = QLineEdit(self.centralwidget)
        self.main_line_p.setObjectName(u"main_line_p")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.main_line_p)

        self.main_prime_q = QLabel(self.centralwidget)
        self.main_prime_q.setObjectName(u"main_prime_q")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.main_prime_q)

        self.main_line_q = QLineEdit(self.centralwidget)
        self.main_line_q.setObjectName(u"main_line_q")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.main_line_q)

        self.main_N = QLabel(self.centralwidget)
        self.main_N.setObjectName(u"main_N")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.main_N)

        self.main_line_N = QLineEdit(self.centralwidget)
        self.main_line_N.setObjectName(u"main_line_N")
        self.main_line_N.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.main_line_N)

        self.main_phi = QLabel(self.centralwidget)
        self.main_phi.setObjectName(u"main_phi")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.main_phi)

        self.main_line_phi = QLineEdit(self.centralwidget)
        self.main_line_phi.setObjectName(u"main_line_phi")
        self.main_line_phi.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.main_line_phi)

        self.main_public = QLabel(self.centralwidget)
        self.main_public.setObjectName(u"main_public")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.main_public)

        self.main_line_public = QLineEdit(self.centralwidget)
        self.main_line_public.setObjectName(u"main_line_public")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.main_line_public)

        self.main_privite = QLabel(self.centralwidget)
        self.main_privite.setObjectName(u"main_privite")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.main_privite)

        self.main_line_private = QLineEdit(self.centralwidget)
        self.main_line_private.setObjectName(u"main_line_private")
        self.main_line_private.setReadOnly(True)
        self.main_line_private.setClearButtonEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.main_line_private)


        self.verticalLayout.addLayout(self.formLayout)

        self.btn_main = QPushButton(self.centralwidget)
        self.btn_main.setObjectName(u"btn_main")

        self.verticalLayout.addWidget(self.btn_main)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFlat(False)

        self.verticalLayout.addWidget(self.btn_clear)

        self.verticalSpacer_3 = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.from_N = QLabel(self.centralwidget)
        self.from_N.setObjectName(u"from_N")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.from_N)

        self.from_line_N = QLineEdit(self.centralwidget)
        self.from_line_N.setObjectName(u"from_line_N")
        self.from_line_N.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.from_line_N)

        self.from_public = QLabel(self.centralwidget)
        self.from_public.setObjectName(u"from_public")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.from_public)

        self.from_line_public = QLineEdit(self.centralwidget)
        self.from_line_public.setObjectName(u"from_line_public")
        self.from_line_public.setReadOnly(False)
        self.from_line_public.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.from_line_public)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label)

        self.from_sign = QLineEdit(self.centralwidget)
        self.from_sign.setObjectName(u"from_sign")
        self.from_sign.setReadOnly(True)
        self.from_sign.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.from_sign)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.btn_encrypt = QPushButton(self.centralwidget)
        self.btn_encrypt.setObjectName(u"btn_encrypt")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_encrypt.sizePolicy().hasHeightForWidth())
        self.btn_encrypt.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn_encrypt)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.to_N = QLabel(self.centralwidget)
        self.to_N.setObjectName(u"to_N")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.to_N)

        self.to_line_N = QLineEdit(self.centralwidget)
        self.to_line_N.setObjectName(u"to_line_N")
        self.to_line_N.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.to_line_N)

        self.to_private = QLabel(self.centralwidget)
        self.to_private.setObjectName(u"to_private")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.to_private)

        self.to_line_private = QLineEdit(self.centralwidget)
        self.to_line_private.setObjectName(u"to_line_private")
        self.to_line_private.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.to_line_private)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.to_sign = QLineEdit(self.centralwidget)
        self.to_sign.setObjectName(u"to_sign")
        self.to_sign.setReadOnly(True)
        self.to_sign.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.to_sign)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.btn_decrypt = QPushButton(self.centralwidget)
        self.btn_decrypt.setObjectName(u"btn_decrypt")

        self.verticalLayout_3.addWidget(self.btn_decrypt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.formLayout_4.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.from_text = QTextEdit(self.centralwidget)
        self.from_text.setObjectName(u"from_text")

        self.verticalLayout_4.addWidget(self.from_text)

        self.to_text = QTextEdit(self.centralwidget)
        self.to_text.setObjectName(u"to_text")

        self.verticalLayout_4.addWidget(self.to_text)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 852, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.open)
        self.menuFile.addAction(self.save)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"lab_13: Signed RSA", None))
        self.open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.open.setToolTip(QCoreApplication.translate("MainWindow", u"Open input file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.save.setToolTip(QCoreApplication.translate("MainWindow", u"Save output text", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.generate_key.setText(QCoreApplication.translate("MainWindow", u"Random Key", None))
#if QT_CONFIG(tooltip)
        self.generate_key.setToolTip(QCoreApplication.translate("MainWindow", u"Generate random P, Q primes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.generate_key.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.main_prime_p.setText(QCoreApplication.translate("MainWindow", u"Prime P:", None))
        self.main_line_p.setInputMask("")
        self.main_prime_q.setText(QCoreApplication.translate("MainWindow", u"Prime Q: ", None))
        self.main_N.setText(QCoreApplication.translate("MainWindow", u"RSA mod N: ", None))
        self.main_phi.setText(QCoreApplication.translate("MainWindow", u"\u03c6(N): ", None))
        self.main_public.setText(QCoreApplication.translate("MainWindow", u"Public Key (E): ", None))
        self.main_privite.setText(QCoreApplication.translate("MainWindow", u"Private Key (D): ", None))
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(shortcut)
        self.btn_main.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.from_N.setText(QCoreApplication.translate("MainWindow", u"RSA mod N: ", None))
        self.from_public.setText(QCoreApplication.translate("MainWindow", u"Public Key (E): ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sign:", None))
        self.btn_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.to_N.setText(QCoreApplication.translate("MainWindow", u"RSA mod N: ", None))
        self.to_private.setText(QCoreApplication.translate("MainWindow", u"Private Key (D): ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign:", None))
        self.btn_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

