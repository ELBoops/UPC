from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


from gui.screens.main_screen import MainScreen
from gui.screens.physic_screen.main_physic_screen import PhysicsScreen
from gui.screens.math_screen.main_maths_screen import MathsScreen
# from gui.screens.physic_screen.mechanics_screen import MechanicsScreen
# from gui.screens.physic_screen.optic_screen import OpticsScreen
# from gui.screens.physic_screen.electrodynamic_screen import ElectrodynamicsScreen
# from gui.screens.physic_screen.thermodynamic_screen import ThermodynamicsScreen

class PhysicsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(PhysicsScreen(name="physics"))
        sm.add_widget(MathsScreen(name="maths"))
        # sm.add_widget(ElectrodynamicsScreen(name="electrodynamics"))
        # sm.add_widget(ThermodynamicsScreen(name="thermodynamics"))
        sm.current = "main"
        return sm