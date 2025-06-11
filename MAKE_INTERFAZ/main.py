from PyQt5.QtWidgets import QApplication, QLabel
from controlando_tamano_ventana import ListenerKeyboard

def funcion1():
    print("Funcion 1, se ejecuto")

def funcion2():
    print("Funcion 2, se ejecuto")

listener = ListenerKeyboard()
listener.run_fun(['a'], funcion1)
listener.run_fun(['b'], funcion2)
listener.quit_program(['<esc>'])
listener.running_loop()


"""
app = QApplication([])
label = QLabel('¡Hola, PyQt5!')
label.show()
app.exec()

"""
