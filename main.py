from kivy.app import App
from kivy.uix.widget import Widget


class ClockedWindow(Widget):
    pass


class ClockedApp(App):
    def build(self):
        self.icon = r'Assets/images/ClockedLogo.png'
        return ClockedWindow()


if __name__ == '__main__':
    ClockedApp().run()
