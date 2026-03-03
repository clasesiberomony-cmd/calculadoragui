from PyQt5 import QtWidgets,uic

class VentanaCalculadora(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_calculadora.ui",self)
        self.show()
        
        self.boton_sumar.clicked.connect(self.sumarNumeros)
        
    def sumarNumeros(self):
        #extraer los datos desde la interfaz
        num1 = int(self.edit_numero1.text())
        num2 = int(self.edit_numero2.text())
        suma = num1 + num2
        self.label_resultado.setText(str(suma))