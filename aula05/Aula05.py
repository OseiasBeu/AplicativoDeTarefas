from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super(Tarefas, self).__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa,font_size=30))


class Teste(App):
    def build(self):
        return Tarefas(['novo item',"Fazer compras",'Buscar filho','novo item'], orientation='horizontal')

Teste().run()

