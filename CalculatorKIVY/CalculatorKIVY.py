from kivy.app import App
from kivy.a=lang.builder import Builder


class CalculatorApp(App):

    def build(self):
        return Builder.load_file("calc.kv")

calcApp = CalculatorApp()
calcApp.run()