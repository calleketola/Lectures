import tkinter as tk

app = tk.Tk()
min_widget1 = tk.Label(app, text="1")
min_widget2 = tk.Label(app, text="2")
min_widget3 = tk.Label(app, text="3")
min_widget4 = tk.Label(app, text="4")

min_widget1.place(x=50, y=20)
min_widget2.place(x=20, y=20)
min_widget3.place(x=20, y=50)
min_widget4.place(x=50, y=50)
