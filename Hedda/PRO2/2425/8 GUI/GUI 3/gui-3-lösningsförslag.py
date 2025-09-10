import json
import tkinter as tk

class App():

    def __init__(self):
        self.root = tk.Tk()

        self.create_widgets()
        self.place_start_widgets()

        self.root.mainloop()

    def create_widgets(self):
        self.file_field = tk.Entry(self.root)
        self.load_file_button = tk.Button(self.root, text="Ladda fil", command=self.load_file)

        self.movie_list = tk.Listbox(self.root)
        self.load_movie_button = tk.Button(self.root, text="Ladda film", command=self.load_movie)
        self.hide_movie_button = tk.Button(self.root, text="Göm film", command=self.hide_movie)

    def place_start_widgets(self):
        self.file_field.grid(row=0, column=0)
        self.load_file_button.grid(row=0, column=1)

    def choose_file(self):
        file = fd.askopenfilenames(initialdir="/",title="Välj fil")

    def load_file(self):
        file_name = self.file_field.get()

        with open(file_name) as f:
            self.movies = json.load(f)
    
        self.show_list_widgets()
        self.movie_labels = []

    def show_list_widgets(self):
        self.movie_list["height"] = len(self.movies)

        print("yo")

        for i in range(len(self.movies)):
            self.movie_list.insert(tk.END, self.movies[i]["title"])

        self.movie_list.grid(row=1, column=0,rowspan=len(self.movies))
        self.load_movie_button.grid(row=1, column=1)
        self.hide_movie_button.grid(row=2, column=1)

    def load_movie(self):

        self.hide_movie()
        
        movie = self.movie_list.curselection()[0]

        self.movie_labels = []
        for key in self.movies[movie]:
            self.movie_labels.append([])
            
            self.movie_labels[-1].append(tk.Label(self.root, text=key))
            self.movie_labels[-1].append(tk.Label(self.root, text=self.movies[movie][key]))

        # Place widgets
        for i in range(len(self.movie_labels)):
            self.movie_labels[i][0].grid(row=i,column=2)
            self.movie_labels[i][1].grid(row=i,column=3)

    def hide_movie(self):
        for i in range(len(self.movie_labels)):
            self.movie_labels[i][1].destroy()
            self.movie_labels[i][0].destroy()

app = App()
