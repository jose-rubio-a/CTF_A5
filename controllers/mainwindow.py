import json, time, threading
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from views.Ui_notas import Ui_MainWindow
from PySide2.QtCore import Slot, QThread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ubicacion = ""

        self.abrir_temp()
        self.hilo2 = threading.Thread(target=self.temp, daemon=True)
        self.hilo2.start()

        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.actionGuardar_como.triggered.connect(self.action_guardar_como_archivo)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionNuevo.triggered.connect(self.action_nuevo)
        
    def guardar(self, ubicacion):
        try:
            archivo = open(ubicacion, 'w')
            texto = self.ui.plainTextEdit.toPlainText()
            archivo.write(texto)
            archivo.close()
            self.setWindowTitle(ubicacion)
            self.ubicacion = ubicacion
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            archivo = open(ubicacion, 'r')
            texto = archivo.read()
            self.ui.plainTextEdit.setPlainText(texto)
            self.ubicacion = ubicacion
            self.setWindowTitle(ubicacion)
            return 1
        except:
            return 0
    
    @Slot()
    def action_guardar_archivo(self):
        if self.ubicacion == "":
            ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'TXT (*.txt)')[0]
        else:
            ubicacion = self.ubicacion
        if self.guardar(ubicacion):
            QMessageBox.information(self, "Exito", "Se creo el archivo " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el archivo " + ubicacion)
    
    @Slot()
    def action_guardar_como_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'TXT (*.txt)')[0]
        if self.guardar(ubicacion):
            QMessageBox.information(self, "Exito", "Se creo el archivo " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el archivo " + ubicacion)
    
    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(self,'Abrir Archivo','.','TXT (*.txt)')[0]
        if self.abrir(ubicacion):
            QMessageBox.information(self, "Exito", "Se abrio el archivo " + ubicacion)
        else:
            QMessageBox.critical(self,"Error" , "Error al abrir el archivo " + ubicacion)
    
    @Slot()
    def action_nuevo(self):
        self.ubicacion = ""
        self.setWindowTitle("Sin Nombre")
        self.ui.plainTextEdit.setPlainText("")

    def temp(self):
        while True:
            try:
                with open("./respaldo.json", 'w') as archivo:
                    lista = [
                        {
                            "Nombre": self.ubicacion,
                            "texto": self.ui.plainTextEdit.toPlainText()
                        }
                    ]
                    json.dump(lista, archivo, indent=5)
                time.sleep(5)
            except:
                raise Exception("Error: al guardar archivo temp")
    
    def abrir_temp(self):
        try:
            with open("./respaldo.json", 'r') as archivo:
                lista = json.load(archivo)
                if lista[0]['Nombre'] != "":
                    self.ubicacion = lista[0]['Nombre']
                    self.setWindowTitle(self.ubicacion)
                self.ui.plainTextEdit.setPlainText(lista[0]['texto'])
        except:
            raise Exception("Error: al cargar archivo temp")