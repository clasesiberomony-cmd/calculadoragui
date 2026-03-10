from PyQt5 import QtWidgets,uic
#Referencia a la clase
from load.load_venta_calculadora import VentanaCalculadora


class MenuPricipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #Llamar a la interfaz del menu
        uic.loadUi("gui/menu_principal.ui",self)
        self.showMaximized()
        
        #Llamar a la ventana calculadora
        self.actionCalculadora.triggered.connect(self.ingresarCalculadora)
        self.actionSalir_2.triggered.connect(self.salir)
     
        
    def ingresarCalculadora(self):
        #Crear objeto de la clase ventanaCalculadora
        vc = VentanaCalculadora()
        #abrir la ventana
        vc.exec()
        
    def salir(self):
        self.close()