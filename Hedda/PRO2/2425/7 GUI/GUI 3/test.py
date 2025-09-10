import tkinter as tk
class App():
    def __init__(self):
        self.root = tk.Tk() # Skapa fösntret
        
        self.create_widgets()
        self.place_widgets()
        
        self.root.mainloop()

    def create_widgets(self):
        """
        Metod som skapar alla widgets
        """
        self.file_entry = tk.Entry(self.root)
        self.load_file_button = tk.Button(self.root, text="Ladda fil", command=self.load_file)
        self.text_label = tk.Label(self.root, text="")

    def place_widgets(self):
        """
        Metod som placerar ut alla widgets
        """
        self.file_entry.grid(row=0, column=0)
        self.load_file_button.grid(row=0, column=1)
        self.text_label.grid(row=1,column=0, columnspan=2)

    def load_file(self):
        file_name = self.file_entry.get()
        with open(file_name, encoding="utf-8") as f:
            self.data = f.readlines()
        self.text_label["text"] = self.data[0]

app = App()
