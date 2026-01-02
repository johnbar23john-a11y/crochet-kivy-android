import os, json, re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import platform

# Android storage permission
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE])

# Optional PDF support
try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None

STITCH_COLORS = {
    "sc": "2ecc71",
    "dc": "3498db",
    "hdc": "e67e22",
    "inc": "f1c40f",
    "dec": "e74c3c"
}

SAVE_FILE = "crochet_progress.json"


class CrochetUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.pattern = []
        self.line = 0
        self.stitch = 0
        self.current_file = None

        # Row counter
        self.row_label = Label(
            text="Load a pattern",
            size_hint_y=None,
            height=60,
            font_size=24
        )
        self.add_widget(self.row_label)

        # Pattern display
        self.text_label = Label(
            text="",
            markup=True,
            font_size=28,
            size_hint_y=None,
            valign="top"
        )
        self.text_label.bind(
            texture_size=lambda i, v: setattr(i, "height", v[1])
        )

        scroll = ScrollView()
        scroll.add_widget(self.text_label)
        self.add_widget(scroll)

        # Controls
        controls = BoxLayout(size_hint_y=None, height=90)

        for txt, fn in [
            ("◀", self.prev_stitch),
            ("▶", self.next_stitch),
            ("▲", self.prev_line),
            ("▼", self.next_line),
            ("📂", self.open_file),
        ]:
            controls.add_widget(
                Button(text=txt, font_size=32, on_press=fn)
            )

        self.add_widget(controls)

        Window.bind(on_key_down=self.on_key)

    # ---------- Keyboard ----------
    def on_key(self, window, key, *args):
        if key in (32, 275):   # space / right
            self.next_stitch()
        elif key in (8, 276): # backspace / left
            self.prev_stitch()

    # ---------- File loading ----------
    def open_file(self, *args):
        chooser = FileChooserIconView(
            filters=["*.txt", "*.csv", "*.pdf"]
        )
        popup = Popup(
            title="Select Pattern",
            content=chooser,
            size_hint=(0.9, 0.9)
        )
        chooser.bind(
            on_submit=lambda c, s, t: self.load_file(s[0], popup)
        )
        popup.open()

    def load_file(self, path, popup):
        popup.dismiss()
        self.current_file = os.path.abspath(path)

        if path.lower().endswith(".pdf") and PdfReader:
            text = self.load_pdf(path)
        else:
            with op
