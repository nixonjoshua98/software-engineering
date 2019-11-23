import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from news_api import NewsAPI
from spotify_api import SpotifyAPI

# Python 3.7.4

# pip install newsapi-python
# pip install spotipy
# pip install rake-nltk

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window attributes
        self.title("Spotify News Recommendations")
        self.geometry("390x380")
        self.update()        
        self.minsize(self.winfo_width(), self.winfo_height())        
        self.config(bg="white")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        # Attribute widget
        self.tree = None
        self.category_dd = None
        self.country_dd = None

        # API
        self.news_api = NewsAPI()
        self.spotify_api = SpotifyAPI(" ")

        # Widget creation
        self.create_menu()
        self.create_title()
        self.create_results_tree()

    # Callback for window close
    def on_exit(self):
        if messagebox.askyesno("Exit Application", "Are you sure?"):
            self.destroy()
            self.quit()

    def on_search_btn(self):
        keywords = self.news_api.get_keywords(1, self.country_dd.get().lower(), self.category_dd.get().lower())

        # Tell the user an issue happened
        if len(keywords) == 0:
            messagebox.showinfo("Keywords", "No keywords found.")
            return

        tracks = self.spotify_api.search_for_tracks(keywords)

        # Tell the user an issue happened
        if len(tracks) == 0:
            messagebox.showinfo("Spotify Tracks", "No tracks found - Try again.")
            return

        self.tree.delete(*self.tree.get_children())

        for t in tracks:
            self.tree.insert("", "end", values = (", ".join(t.artists), t.album, t.name))

        
    def create_menu(self):
        frame = tk.Frame(self, bg="white")
        
        self.country_dd = ttk.Combobox(frame, state="readonly")
        self.country_dd["values"]=["GB", "US"]
        self.country_dd.current(0)

        self.category_dd = ttk.Combobox(frame, state="readonly")
        self.category_dd["values"]=["General", "Health", "Science", "Sports", "Technology", "Business", "Entertainment"]
        self.category_dd.current(0)

        self.category_dd.pack(side=tk.LEFT, fill=tk.X, padx=5, fil=tk.X, expand=True)        
        self.country_dd.pack(side=tk.LEFT, fil=tk.X, expand=True)

        frame.pack(fill=tk.X, padx=25)

        btn = ttk.Button(self, text="Search", command=self.on_search_btn)

        btn.pack(pady=10)

    def create_title(self):
        frame = tk.Frame(self, bg="white")
        label = tk.Label(frame, text="Search Results", bg="white", font=("Ariel", 16))

        label.pack(side=tk.LEFT, fill=tk.X, padx=5)
        frame.pack(fill=tk.X)

    def create_results_tree(self):
        frame = tk.Frame(self, bg="white")
        
        self.tree = ttk.Treeview(frame,
                            columns=["Artist(s)", "Album", "Track"],
                            show="headings")
                            
        scroll = ttk.Scrollbar(self)

        for i, col in enumerate(self.tree["columns"]):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=1)

        self.tree.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.tree.yview)
        
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

app = Application()

app.mainloop()
