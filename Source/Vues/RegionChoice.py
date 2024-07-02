import tkinter as tk
from Source.Global import Global
from Source.Controllers.RegionChoiceController import RegionChoiceController
from Source.Views.Map import Map

class RegionChoice(tk.Tk):
    """
    Class representing the region selection window.

    Inherits from tk.Tk and uses the RegionChoiceController to manage
    interactions and data.

    Attributes:
    -----------
    controller : RegionChoiceController
        Instance of RegionChoiceController to manage interactions and data.

    Methods:
    --------
    __init__(disease):
        Initializes the region selection window with the given disease.
    create_buttons():
        Creates buttons for each available region.
    create_static_elements():
        Creates the static elements of the window (title).
    open_map(event):
        Opens the map window after selecting a region.
    setup():
        Configures the main region selection window.
    """

    def __init__(self, disease):
        """
        Initializes the region selection window.

        Parameters:
        ------------
        disease : object
            Instance of the Disease class.
        """
        super().__init__()
        self.controller = RegionChoiceController(disease)
        self.attributes('-alpha', 0.0)
        self.setup()
        self.create_buttons()
        self.create_static_elements()
        self.attributes('-alpha', 1.0)

    def create_buttons(self):
        """
        Creates buttons for each available region and configures their placement.
        """
        for i, region in enumerate(self.controller.get_regions()):
            self.button = tk.Button(
                self, text=region, background="dark grey", font=("Courier", 18),
                borderwidth=0, highlightthickness=0)
            tk.Grid.columnconfigure(self, i % 4 + 2, weight=1)
            self.button.grid(row=i // 4 + 2, column=i % 4 + 1, padx=10, pady=10)
            self.button.bind("<ButtonRelease-1>", self.open_map)
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 5, weight=1)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 7, weight=2)

    def create_static_elements(self):
        """
        Creates the static elements of the window (title).
        """
        tk.Grid.rowconfigure(self, 1, weight=1)
        self.title_label = tk.Label(
            self, text="Please choose the first region to infect",
            font=("Courier", 30, "bold"), background="black", foreground="white")
        self.title_label.grid(row=1, column=1, columnspan=4)

    def open_map(self, event):
        """
        Opens the map window after selecting a region.

        Parameters:
        ------------
        event : tk.Event
            The event triggered upon region selection.
        """
        disease = self.controller.get_disease()
        world = self.controller.get_world()
        region = event.widget["text"]
        self.destroy()
        self.controller.choose_region(region)
        _ = Map(disease, world)

    def setup(self):
        """
        Configures the main region selection window.
        """
        Global().set_fullscreen(self)
        self.configure(background="black")
        self.title("COVID-24")