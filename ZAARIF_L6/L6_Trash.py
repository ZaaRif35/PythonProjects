from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        label = Label(text="Hello from kivy",
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        img = Image(source='https://www.google.com/url?sa=i&url=https%3A%2F%2Fjoke-battles.fandom.com%2Fwiki%2FGigachad&psig=AOvVaw2P9j3lDCVyaD2lw1Koa5G9&ust=1733730855789000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNjEoN_al4oDFQAAAAAdAAAAABAE',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y':.5})

        return img


if __name__ == '__main__':
    app = MainApp()
    app.run()


MainApp().run()