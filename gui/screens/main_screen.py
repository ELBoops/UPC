from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bl = BoxLayout(orientation="vertical", spacing=20, padding=40)
        
        def chage_screen(screen_name):
            def change_screen_inner(instance):
                self.run_gui(screen_name)
            return change_screen_inner

        bl.add_widget(Label(
            text="Выберите предмет",
            font_size=32,
            size_hint=(1, .2),
        ))
        
        bl.add_widget(Button(
            text="Maths",
            on_press= lambda x: self.go_to("maths_screens"),
            
        ))

        bl.add_widget(Button(
            text="Physics",
            on_press=lambda x: self.go_to("physics_screen")
        ))

        bl.add_widget(Button(
            text="Chemistry",
            on_press=lambda x: self.go_to("chemistry_screen")
        ))

        bl.add_widget(Button(
            text="Custom",
            on_press=lambda x: self.go_to("custom_screen")
        ))

        self.add_widget(bl)

    def go_to(self, screen_name):
        self.manager.current = screen_name