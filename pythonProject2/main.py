import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import MainScreen, ConfigurationScreen, ViewConfigurationScreen, CompatibilityScreen

kivy.require('2.0.0')

# Главное приложение
class PCConfiguratorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(ConfigurationScreen(name='config_screen'))
        sm.add_widget(ViewConfigurationScreen(name = 'view_config_screen'))
        sm.add_widget(CompatibilityScreen(name='compatibility_screen'))
        return sm

if __name__ == '__main__':
    PCConfiguratorApp().run()