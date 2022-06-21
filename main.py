from kivy.app import App
from kivy.uix.widget import Widget


class SufiGame(Widget):
    pass


class SufiApp(App):
    def build(self):
        return SufiGame()


if __name__ == '__main__':
    SufiApp().run()
