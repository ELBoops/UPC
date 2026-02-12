from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bl = BoxLayout(orientation="vertical", spacing=20, padding=40)

        bl.add_widget(Label(
            text="Выберите предмет",
            font_size=32,
            size_hint=(1, .2),
        ))
        
        bl.add_widget(Button(
            text="Maths",
        ))

        bl.add_widget(Button(
            text="Physics",
        ))

        bl.add_widget(Button(
            text="Chemistry",
        ))

        bl.add_widget(Button(
            text="Custom",
        ))

        self.add_widget(bl)

    def run_gui(self, screen_name):
        self.manager.current = screen_name