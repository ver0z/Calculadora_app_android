from kivymd.app import MDApp
import kivymd.uix.button
import kivymd.uix.label
import kivy.uix.textinput
import kivymd.uix.boxlayout
import numpy
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.uix.button import MDFloatingActionButton

Builder.load_file('calc.kv')


class TestApp(MDApp):

    def add_nums(self, btn):
        num1 = numpy.asfarray(self.input1.text, float)
        num2 = numpy.asfarray(self.input2.text, float)
        result = num1 + num2
        self.lbl.text = str(result)

    def build(self):
        self.input1 = kivy.uix.textinput.TextInput(hint_text="Digite o primeiro número", font_size=18)
        self.input2 = kivy.uix.textinput.TextInput(hint_text="Digite o segundo número", font_size=18)

        self.lbl = kivymd.uix.label.Label(text="Resultado da Soma", color=(0, 0, 0, 1))

        self.btn = MDFloatingActionButton(icon="plus", elevation_normal=12, pos_hint={'center_x':0.5, 'center_y':0.5}, md_bg_color=(0,0,0,0))


        self.btn.bind(on_press=self.add_nums)

        layout = kivymd.uix.boxlayout.BoxLayout(orientation="vertical")

        layout.add_widget(self.input1)
        layout.add_widget(self.input2)

        layout.add_widget(self.lbl)
        layout.add_widget(self.btn)

        return layout


app = TestApp()
app.run()