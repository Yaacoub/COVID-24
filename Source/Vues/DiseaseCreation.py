import tkinter as tk
from Source.Global import Global
from Source.Controllers.DiseaseCreationController import DiseaseCreationController
from Source.Views.RegionChoice import RegionChoice

class DiseaseCreation(tk.Tk):
    """
    Class representing the disease creation window in the COVID-24 application.

    Inherits from:
    -----------
    tk.Tk : Base class for creating Tkinter windows.

    Attributes:
    -----------
    controller : DiseaseCreationController
        Controller to manage disease creation.
    disease_name : tk.StringVar
        Tkinter variable to store the disease name.
    entry : tk.Entry
        Entry field for entering the disease name.
    title_label : tk.Label
        Label displaying the window's title.
    create_button : tk.Button
        Button to validate disease creation and proceed to the next step.

    Methods:
    ----------
    __init__() :
        Initializes the disease creation window and configures its elements.
    create_entry() :
        Creates and places the entry field for the disease name.
    create_elements() :
        Creates and places the window elements like labels and buttons.
    clear_entry(event) :
        Clears the content of the entry field.
    open_region_choice() :
        Closes the current window and opens the region selection window.
    setup() :
        Configures the window for fullscreen display and sets the title and background.
    """

    def __init__(self):
        """
        Initializes the disease creation window and configures its elements.
        """
        super().__init__()
        self.controller = DiseaseCreationController()
        self.disease_name = tk.StringVar(self, "COVID-24")
        self.attributes('-alpha', 0.0)
        self.setup()
        self.create_elements()
        self.after(1, self.create_entry)
        self.attributes('-alpha', 1.0)

    def create_entry(self):
        """
        Creates and places the entry field for the disease name.
        """
        tk.Grid.rowconfigure(self, 1, weight=1)
        self.entry = tk.Entry(
            self, textvariable=self.disease_name, font=("Courier", 30),
            borderwidth=0, highlightthickness=0, background="white")
        self.entry.grid(row=1, column=0)
        self.entry.bind("<FocusIn>", self.clear_entry)

    def create_elements(self):
        """
        Creates and places the window elements like labels and buttons.
        """
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.title_label = tk.Label(
            self, text="Please create your disease to harm humanity",
            font=("Courier", 30, "bold"), background="black", foreground="white")
        self.title_label.grid(row=0, column=0, columnspan=3)

        tk.Grid.rowconfigure(self, 2, weight=1)
        self.create_button = tk.Button(
            self, text="Next", font=("Courier", 18, "bold"), borderwidth=0,
            highlightthickness=0, pady=10, command=self.open_region_choice)
        self.create_button.grid(row=2, column=0, padx=10, pady=10)

    def clear_entry(self, _):
        """
        Clears the content of the entry field.

        Parameters:
        ------------
        event : tk.Event
            The focus event on the entry field.
        """
        self.entry.delete(0, tk.END)

    def open_region_choice(self):
        """
        Closes the current window and opens the region selection window.
        """
        self.destroy()
        self.controller.create_disease(self.disease_name.get())
        _ = RegionChoice(self.controller.get_disease())

    def setup(self):
        """
        Configures the window for fullscreen display and sets the title and background.
        """
        Global().set_fullscreen(self)
        self.configure(background="black")
        self.title("COVID-24")