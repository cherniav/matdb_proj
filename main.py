# Imports and such
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from your_database_api import DatabaseAPI

class MaterialApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.db = DatabaseAPI()
        self.materials = self.db.get_materials()
        self.properties = self.db.get_properties()
        self.selected_materials = []
        self.selected_properties = []
        self.create_widgets()

def create_widgets(self):
    self.material_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
    for material in self.materials:
        self.material_listbox.insert(tk.END, material)
    self.material_listbox.pack(side=tk.LEFT)

    self.property_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
    for property in self.properties:
        self.property_listbox.insert(tk.END, property)
    self.property_listbox.pack(side=tk.LEFT)

    self.plot_button = ttk.Button(self, text="Plot", command=self.plot)
    self.plot_button.pack(side=tk.LEFT)

    self.figure = plt.Figure(figsize=(5, 4), dpi=100)
    self.canvas = FigureCanvasTkAgg(self.figure, self)
    self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

def plot(self):
    self.selected_materials = [self.materials[i] for i in self.material_listbox.curselection()]
    self.selected_properties = [self.properties[i] for i in self.property_listbox.curselection()]

    if len(self.selected_materials) == 0 or len(self.selected_properties) != 2:
        return

    data = self.db.get_data(self.selected_materials, self.selected_properties)

    self.figure.clear()
    ax = self.figure.add_subplot(111)
    for material in data:
        ax.plot(data[material][self.selected_properties[0]], data[material][self.selected_properties[1]], label=material)
    ax.legend()
    self.canvas.draw()

# Main