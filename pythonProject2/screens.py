import kivy
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from data import COMPONENT_DATA, CONFIGURATIONS
from utils import check_compatibility

kivy.require('2.0.0')


# Класс главного экрана
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.config_list = Label(text="Сохраненные конфигурации:", font_size=20, size_hint_y=None, height=50)
        layout.add_widget(self.config_list)

        self.config_list_layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.config_list_layout)
        self.update_config_list()

        create_button = Button(text='Создать новую конфигурацию', size_hint_y=None, height=50)
        create_button.bind(on_press=self.go_to_config_screen)
        layout.add_widget(create_button)

        self.add_widget(layout)

    def update_config_list(self):
        self.config_list_layout.clear_widgets()
        if CONFIGURATIONS:
            for name, config in CONFIGURATIONS.items():
                config_button = Button(text=name, size_hint_y=None, height=40)
                config_button.bind(on_press=lambda instance, name=name: self.go_to_view_config_screen(name))
                self.config_list_layout.add_widget(config_button)

    def go_to_config_screen(self, instance):
        self.manager.current = 'config_screen'

    def go_to_view_config_screen(self, name):
        self.manager.get_screen('view_config_screen').set_config_name(name)
        self.manager.current = 'view_config_screen'


# Класс экрана конфигурации
class ConfigurationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_components = {}

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Название конфигурации
        layout.add_widget(Label(text="Название конфигурации:", font_size=18))
        self.config_name_input = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.config_name_input)

        # Списки выбора компонентов
        for component_type in COMPONENT_DATA.keys():
            layout.add_widget(Label(text=f"{component_type.capitalize()}:", font_size=16))
            spinner = Spinner(text='Выберите ' + component_type, values=COMPONENT_DATA[component_type],
                              size_hint_y=None, height=40)
            spinner.bind(
                text=lambda instance, value, component_type=component_type: self.on_component_selected(component_type,
                                                                                                       value))
            layout.add_widget(spinner)

        # Кнопки управления
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        save_button = Button(text='Сохранить')
        save_button.bind(on_press=self.save_configuration)
        button_layout.add_widget(save_button)

        compatibility_button = Button(text='Проверить совместимость')
        compatibility_button.bind(on_press=self.check_compatibility)
        button_layout.add_widget(compatibility_button)

        cancel_button = Button(text='Отмена')
        cancel_button.bind(on_press=self.go_to_main_screen)
        button_layout.add_widget(cancel_button)
        layout.add_widget(button_layout)

        self.add_widget(layout)

    def on_component_selected(self, component_type, value):
        self.selected_components[component_type] = value

    def save_configuration(self, instance):
        config_name = self.config_name_input.text.strip()
        if config_name and self.selected_components:
            CONFIGURATIONS[config_name] = self.selected_components
            self.clear_config()
            self.go_to_main_screen(instance)

    def clear_config(self):
        self.selected_components = {}
        self.config_name_input.text = ''

    def go_to_main_screen(self, instance):
        self.clear_config()
        self.manager.get_screen('main_screen').update_config_list()
        self.manager.current = 'main_screen'

    def check_compatibility(self, instance):
        self.manager.get_screen('compatibility_screen').set_config_components(self.selected_components)
        self.manager.current = 'compatibility_screen'


class ViewConfigurationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_name = ''
        self.config_data = {}
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.config_name_label = Label(text="", font_size=24, size_hint_y=None, height=60)
        layout.add_widget(self.config_name_label)

        self.components_layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.components_layout)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        edit_button = Button(text="Редактировать")
        edit_button.bind(on_press=self.go_to_config_screen)
        button_layout.add_widget(edit_button)

        back_button = Button(text="Назад")
        back_button.bind(on_press=self.go_to_main_screen)
        button_layout.add_widget(back_button)

        layout.add_widget(button_layout)

        self.add_widget(layout)

    def set_config_name(self, name):
        self.config_name = name
        self.config_name_label.text = f"Конфигурация: {name}"
        self.config_data = CONFIGURATIONS.get(name, {})
        self.update_components_list()

    def update_components_list(self):
        self.components_layout.clear_widgets()
        if self.config_data:
            for component_type, component in self.config_data.items():
                self.components_layout.add_widget(
                    Label(text=f"{component_type.capitalize()}: {component}", font_size=18, size_hint_y=None,
                          height=40))
        else:
            self.components_layout.add_widget(Label(text="Нет данных", font_size=18))

    def go_to_main_screen(self, instance):
        self.manager.current = "main_screen"

    def go_to_config_screen(self, instance):
        self.manager.get_screen("config_screen").config_name_input.text = self.config_name
        self.manager.get_screen("config_screen").selected_components = self.config_data
        self.manager.current = "config_screen"


class CompatibilityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_components = {}
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.compatibility_result = Label(text="Здесь будет результат проверки совместимости", font_size=18)
        layout.add_widget(self.compatibility_result)

        back_button = Button(text="Назад", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_to_config_screen)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def set_config_components(self, components):
        self.config_components = components
        self.check_compatibility()

    def check_compatibility(self):
        result_text = check_compatibility(self.config_components)
        self.compatibility_result.text = result_text

    def go_to_config_screen(self, instance):
        self.manager.current = "config_screen"
