# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 587)
        icon = QIcon()
        icon.addFile(u"./assets/icon/lapiz.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionNuevo = QAction(MainWindow)
        self.actionNuevo.setObjectName(u"actionNuevo")
        self.actionGuardar_como = QAction(MainWindow)
        self.actionGuardar_como.setObjectName(u"actionGuardar_como")
        self.actionNueva_Ventana = QAction(MainWindow)
        self.actionNueva_Ventana.setObjectName(u"actionNueva_Ventana")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 828, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuArchivo.addAction(self.actionAbrir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sin Nombre", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
#if QT_CONFIG(shortcut)
        self.actionNuevo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_como.setText(QCoreApplication.translate("MainWindow", u"Guardar como", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_como.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNueva_Ventana.setText(QCoreApplication.translate("MainWindow", u"Nueva Ventana", None))
#if QT_CONFIG(shortcut)
        self.actionNueva_Ventana.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

