from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


from gui.screens.main_screen import MainScreen
from gui.screens.mechanics_screen import MechanicsScreen
from gui.screens.optic_screen import OpticsScreen
from gui.screens.electrodynamic_screen import ElectrodynamicsScreen
from gui.screens.thermodynamic_screen import ThermodynamicsScreen

class PhysicsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        # sm.add_widget(MechanicsScreen(name="mechanics"))
        # sm.add_widget(OpticsScreen(name="optics"))
        # sm.add_widget(ElectrodynamicsScreen(name="electrodynamics"))
        # sm.add_widget(ThermodynamicsScreen(name="thermodynamics"))
        sm.current = "main"
        return sm