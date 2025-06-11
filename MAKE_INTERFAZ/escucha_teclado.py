from pynput import keyboard

class KeyPrinter:
    def __init__(self):
        pass

    def _key_to_str(self, key):
        try:
            # Teclas normales
            return key.char.lower()
        except AttributeError:
            # Teclas especiales
            return f'<{key.name.lower()}>'

    def _on_press(self, key):
        k = self._key_to_str(key)
        print(k)

    def run(self):
        print("Listener iniciado. Presiona cualquier tecla...")
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()

if __name__ == "__main__":
    kp = KeyPrinter()
    kp.run()
