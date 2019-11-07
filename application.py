import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

    def create_interface(self) -> None: ...

    def show_input_screen(self) -> None: ...

    def show_output_screen(self) -> None: ...
