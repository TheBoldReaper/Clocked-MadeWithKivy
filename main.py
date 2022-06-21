from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer


class ClockedWindow(Widget):
    pass


class ClockedApp(App):
    # Window Properties
    title = "HEHE"
    icon = r'Assets/images/ClockedLogo.png'

    def build(self):
        player = VideoPlayer(source="Assets/images/Neva.mp4")
        player.state = 'play'
        player.options = {'eos': 'loop'}  # eos stands for End of String, In which this is referring what happens when
        # the video ends

        return player


if __name__ == '__main__':
    ClockedApp().run()
