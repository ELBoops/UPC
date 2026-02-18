from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition


from gui.screens.main_screen import MainScreen
from gui.screens.physic_screen.main_physic_screen import PhysicsScreen
from gui.screens.math_screen.main_maths_screen import MathsScreen
from gui.screens.chemistry_screen.main_chemistry_screen import ChemistryScreen
from gui.screens.custom_screen.main_custom_screen import CustomScreen

class UPCApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(PhysicsScreen(name="physics_screen"))
        sm.add_widget(MathsScreen(name="maths_screens"))
        sm.add_widget(ChemistryScreen(name="chemistry_screen"))
        sm.add_widget(CustomScreen(name="custom_screen"))
        sm.current = "main"
       
        return sm   