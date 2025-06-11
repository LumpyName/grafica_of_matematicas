from pynput import keyboard

class ListenerKeyboard:
    def __init__(self):
        self._hotkeys = {}  # {frozenset(teclas): funcion}
        self._pressed = set()
        self._quit_combination = frozenset(['q'])
        self._running = False

    def run_fun(self, key_str, func):
        """
        Registra una tecla con una función a ejecutar.

        key_str: cadena que representa una tecla, ej: 'a' o '<esc>'
        func: función sin parámetros que se ejecutará cuando se presione la tecla
        """
        key_processed = key_str.strip().lower()
        # Asegurar formato con < > para teclas especiales
        if len(key_processed) > 1 and not (key_processed.startswith('<') and key_processed.endswith('>')):
            key_processed = f'<{key_processed}>'

        self._hotkeys[frozenset([key_processed])] = func


def quit_program(self, combination=None):
        """
        Define la combinación para terminar el programa.

        combination: lista o tupla de teclas, ej: ['<esc>']
        Si no se define, la combinación por defecto será 'q'
        """
        if combination:
            self._quit_combination = frozenset(k.lower() for k in combination)
        else:
            self._quit_combination = frozenset(['q'])

    def _key_to_str(self, key):
        try:
            # tecla normal
            return key.char.lower()
        except AttributeError:
            # tecla especial, p.ej. Key.ctrl_l
            return f'<{key.name.lower()}>'

    def _on_press(self, key):
        k = self._key_to_str(key)
        print(f"Tecla presionada: {k}")
        self._pressed.add(k)

        # Revisar si es la combinación para salir
        if self._quit_combination.issubset(self._pressed):
            print("Combinación para salir detectada. Terminando listener.")
            self._running = False
            return False  # Detiene el listener

        # Revisar otras combinaciones y ejecutar funciones
        for combo, func in self._hotkeys.items():
            if combo.issubset(self._pressed):
                try:
                    func()
                except Exception as e:
                    print(f"Error ejecutando función para {combo}: {e}")

    def _on_release(self, key):
        k = self._key_to_str(key)
        if k in self._pressed:
            self._pressed.remove(k)

    def running_loop(self):
        """
        Inicia el loop de escucha, bloqueante.
        """
        if not self._quit_combination:
            raise ValueError("No se ha definido la combinación para salir.")

        self._running = True
        print(f"Listener iniciado. Para salir presiona: {self._quit_combination}")
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()

# Ejemplo de uso
if __name__ == "__main__":
    def funcion1():
        print("¡Combinación 1 activada!")

    def funcion2():
        print("¡Combinación 2 activada!")

    listener = ListenerKeyboard()
    listener.run_fun(['<ctrl_l>', 'a'], funcion1)
    listener.run_fun(['<ctrl_l>', 'b'], funcion2)
    listener.quit_program(['<esc>'])  # Para salir, se presiona ESC

    listener.running_loop()
