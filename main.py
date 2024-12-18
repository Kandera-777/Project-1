from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.icon = "Calculator image.png"

        # Create text input field for calculator display
        self.display = TextInput(
            multiline=False,
            font_size=50,
            size_hint=(1,1),
            background_color = "black",
            foreground_color = "white",
            halign= "right",
            readonly = True

        )
        self.add_widget(self.display)

        # Create buttons for calculator
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    font_size=30,
                    size_hint=(1, 1),
                    
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

        # Create clear button
        Clear_button = Button(
            text='Clear',
            font_size=30,
            size_hint=(1, 1)
        )
        Clear_button.bind(on_press=self.clear_display)
        self.add_widget(Clear_button)

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                result = str(eval(self.display.text))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Error'
        else:
            self.display.text += instance.text

    def clear_display(self, instance):
        self.display.text = ''

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()