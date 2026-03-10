
from PyQt5 import QtWidgets
# para poder cargar la interfaz y se pueda cerrar
import sys 
#Referenciar a la clase
from load.load_menu_principal import MenuPricipal

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = MenuPricipal() #Llamar a la ventana del menú principal
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()