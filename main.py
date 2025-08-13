from datetime import datetime, timedelta
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout

class DueDateScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.invoice_date = MDTextField(hint_text="Invoice Date (YYYY-MM-DD)", size_hint_x=1)
        self.term_days = MDTextField(hint_text="Term Days", input_filter="int", size_hint_x=1)

        self.business_days_checkbox = MDCheckbox(size_hint=(None, None))
        checkbox_label = MDLabel(text="Business Days (skip weekends)", size_hint_x=None, width=200)

        checkbox_layout = MDBoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=48)
        checkbox_layout.add_widget(self.business_days_checkbox)
        checkbox_layout.add_widget(checkbox_label)

        self.result_label = MDLabel(text="", halign="center")

        calculate_button = MDRaisedButton(text="Calculate Due Date", pos_hint={"center_x": 0.5}, on_release=self.calculate_due_date)

        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=15)
        layout.add_widget(self.invoice_date)
        layout.add_widget(self.term_days)
        layout.add_widget(checkbox_layout)
        layout.add_widget(calculate_button)
        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def parse_date(self, s):
        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
            try:
                return datetime.strptime(s.strip(), fmt).date()
            except Exception:
                pass
        raise ValueError("Invalid date format")

    def add_business_days(self, start_date, days):
        d = start_date
        added = 0
        while added < days:
            d += timedelta(days=1)
            if d.weekday() < 5:
                added += 1
        return d

    def calculate_due_date(self, instance):
        try:
            inv = self.parse_date(self.invoice_date.text)
        except Exception as e:
            self.result_label.text = f"Error: {e}"
            return
        try:
            n = int(self.term_days.text)
        except Exception:
            self.result_label.text = "Term must be a number"
            return

        if self.business_days_checkbox.active:
            due = self.add_business_days(inv, n)
        else:
            due = inv + timedelta(days=n)

        self.result_label.text = (
            f"Invoice: {inv.strftime('%Y-%m-%d')} ({inv.strftime('%A')})\n"
            f"Due: {due.strftime('%Y-%m-%d')} ({due.strftime('%A')})"
        )

class DueDateApp(MDApp):
    def build(self):
        self.title = "Due Date Calculator"
        self.theme_cls.primary_palette = "Teal"
        return DueDateScreen()

if __name__ == "__main__":
    DueDateApp().run()