from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class PhysicsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bl = BoxLayout(orientation="vertical", spacing=20, padding=40)
        
        def chage_screen(screen_name):
            def change_screen_inner(instance):
                self.run_gui(screen_name)
            return change_screen_inner

        bl.add_widget(Label(
            text="Выберите раздел",
            font_size=32,
            size_hint=(1, .2),
        ))
        
        bl.add_widget(Button(
            text="Mechanics",
            on_press= chage_screen("mechanics_screen")
        ))

        bl.add_widget(Button(
            text="Electrodynamics",
            on_press= chage_screen("electrodynamics_screen")
        ))

        bl.add_widget(Button(
            text="Thermodynamics",
            on_press= chage_screen("thermodynamics_screen"),
             
        ))

        bl.add_widget(Button(
            text="Optics",
            on_press= chage_screen("optics_screen")
        ))

        self.add_widget(bl)

def go_to(self, screen_name):
    self.manager.current = screen_name