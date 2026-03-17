from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import ScrollView
from kivy.metrics import dp

class IRInterpreterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        # Main Layout
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Header
        layout.add_widget(MDLabel(
            text="IR Spectrum Interpreter",
            halign="center",
            font_style="H5",
            size_hint_y=None,
            height=dp(50)
        ))
        
        # Input Field
        self.input_value = MDTextField(
            hint_text="Enter Wavenumber (cm⁻¹)",
            helper_text="Example: 1715 or 3300",
            helper_text_mode="on_focus",
            input_filter="float",
            mode="rectangle"
        )
        layout.add_widget(self.input_value)
        
        # Search Button
        btn = MDRaisedButton(
            text="INTERPRET",
            pos_hint={"center_x": 0.5},
            on_release=self.interpret_ir
        )
        layout.add_widget(btn)
        
        # Result Area
        self.result_label = MDLabel(
            text="Results will appear here.",
            halign="center",
            theme_text_color="Secondary"
        )
        layout.add_widget(self.result_label)
        
        # Quick Reference Database (Visual for User)
        scroll = ScrollView()
        db_label = MDLabel(
            text=(
                "Quick Guide:\n"
                "3200-3600: O-H (Alcohol/Phenol)\n"
                "3300-3500: N-H (Amine/Amide)\n"
                "1700-1750: C=O (Carbonyl)\n"
                "1600-1680: C=C (Alkene)\n"
                "2850-3000: C-H (Alkanes)"
            ),
            size_hint_y=None,
            height=dp(200),
            halign="left"
        )
        scroll.add_widget(db_label)
        layout.add_widget(scroll)
        
        screen = MDScreen()
        screen.add_widget(layout)
        return screen

    def interpret_ir(self, instance):
        try:
            val = float(self.input_value.text)
            result = ""
            
            # Interpretation Logic
            if 3200 <= val <= 3600:
                result = "Strong, Broad: O-H stretch (Alcohol or Phenol)"
            elif 3300 <= val <= 3500:
                result = "Medium: N-H stretch (Amine or Amide)"
            elif 2100 <= val <= 2260:
                result = "Weak/Medium: C≡C or C≡N stretch (Alkyne/Nitrile)"
            elif 1700 <= val <= 1750:
                result = "Strong: C=O stretch (Ketone, Aldehyde, or Ester)"
            elif 1600 <= val <= 1680:
                result = "Medium: C=C stretch (Alkene)"
            elif 1000 <= val <= 1300:
                result = "Strong: C-O stretch (Alcohol, Ester, or Ether)"
            else:
                result = "No major functional group match in this common range."
            
            self.result_label.text = f"Value {val} cm⁻¹:\n{result}"
            self.result_label.theme_text_color = "Primary"
            
        except ValueError:
            self.result_label.text = "Please enter a valid number."
            self.result_label.theme_text_color = "Error"

if __name__ == "__main__":
    IRInterpreterApp().run()
