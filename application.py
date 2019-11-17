import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import functools as ft

import sys
import time

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Spotify News Recommendations")
        self.geometry("500x250")
        self.config(bg="white")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.create_header()

    def create_header(self):
        frame = tk.Frame(self, relief=tk.SUNKEN, borderwidth=1, bg="white")    
        
        title = tk.Label(frame, font=("Ariel", 16, "bold", "underline"), text="Spotify News Recommendations", bg="white")
        clock = tk.Label(frame, font=("Ariel", 16, "bold"), text="[CLOCK]", bg="white", relief=tk.RIDGE)

        title.pack(side=tk.LEFT, padx=5, pady=5)
        clock.pack(side=tk.RIGHT, padx=5, pady=5)
        frame.pack(padx=5, pady=5, fill=tk.X)

        self.update_clock(clock)


    def on_exit(self):
        if messagebox.askyesno("Exit Application", "Are you sure?"):
            self.destroy()
            sys.exit(0)

    # Scheduled task
    def update_clock(self, clock: tk.Text):
        now = time.strftime("%H:%M:%S")
        clock.config(text=now)
        self.after(333, lambda: self.update_clock(clock))
        
app = Application()

app.mainloop()
