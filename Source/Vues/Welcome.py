import tkinter as tk
from Source.Global import Global
from Source.Views.DiseaseCreation import DiseaseCreation

class Welcome(tk.Tk):
    """
    Class representing the welcome window of the COVID-24 application.

    Inherits from:
    --------------
    tk.Tk : Base class for creating Tkinter windows.

    Attributes:
    -----------
    label_title : tk.Label
        Label displaying the application title.
    create_button : tk.Button
        Button to create a new disease.
    label_copyright : tk.Label
        Label displaying copyright information.

    Methods:
    --------
    __init__(self):
        Initializes the welcome window and configures its elements.

    create_welcome(self):
        Configures and places the widgets in the welcome window.

    open_disease(self):
        Destroys the current window and opens the disease creation window.

    setup(self):
        Configures the window for fullscreen display and sets the title and background.
    """

    def __init__(self):
        """
        Initializes the welcome window and configures its elements.
        """
        super().__init__()
        self.setup()
        self.create_welcome()

    def create_welcome(self):
        """
        Configures and places the widgets in the welcome window.
        """
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.label_title = tk.Label(self, text="COVID-24", font=("Courier", 80, "bold"),
                                    background="black", foreground="red")
        self.label_title.grid(row=0, column=0, columnspan=3)

        tk.Grid.rowconfigure(self, 3, weight=1)
        self.create_button = tk.Button(self, text="Create a disease", font=("Courier", 18, "bold"),
                                       borderwidth=0, highlightthickness=0, pady=10,
                                       command=self.open_disease)
        self.create_button.grid(row=2, column=0, padx=10, pady=10)

        text = "Copyright © 2024. Baptiste Gojon, Mathieu Jallerat, Liam Le Touzé, Peter Yaacoub"
        self.label_copyright = tk.Label(self, text=text, font=("Courier", 18, "bold"),
                                        background="black", foreground="grey")
        self.label_copyright.grid(row=5, column=0, columnspan=3)

    def open_disease(self):
        """
        Destroys the current window and opens the disease creation window.
        """
        self.destroy()
        _ = DiseaseCreation()

    def setup(self):
        """
        Configures the window for fullscreen display and sets the title and background.
        """
        Global().set_fullscreen(self)
        self.configure(background="black")
        self.title("COVID-24")