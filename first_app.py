from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class TrialApp(MDApp):
    def build(self):
        label = MDLabel(
            text="Hello, Pepu",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1)  # Red color in RGBA
        )
        return label

TrialApp().run()
