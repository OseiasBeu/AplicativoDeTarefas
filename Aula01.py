from kivy.app import App
from kivy.uix.button import Button

class TesteButton(App):
    def build(self):
        return Button(text='Olá Mundo!!!')

TesteButton().run()

