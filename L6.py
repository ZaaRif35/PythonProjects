import random
from functools import reduce

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExemple(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(10):
            btn = Button(
                text="Button #%s" % (i+1),
                background_color = random.choice(colors),
                color = random.choice(colors)  )

            layout.add_widget(btn)
        return layout


if __name__ == "__main__":
    HBoxLayoutExemple().run()

