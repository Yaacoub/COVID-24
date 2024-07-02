import tkinter as tk
from Source.Global import Global
from Source.Controllers.InformationsController import InformationsController

class Informations(tk.Tk):
    """
    Class representing the information window.

    Inherits from tk.Tk and uses the InformationsController to manage interactions and data.

    Attributes:
    ----------
    controller : InformationsController
        Instance of InformationsController to manage interactions and data.
    close_function : function
        Function to call to close the window.
    stats_labels : list
        List of labels displaying the statistics.

    Methods:
    ---------
    __init__(close_function, disease, world):
        Initializes the information window with instances of close_function, disease, and world.
    create_close_button():
        Creates the button to close the information window.
    create_region_info():
        Creates and updates the region information.
    open_map():
        Closes the information window and returns to the previous window.
    setup():
        Configures the main information window.
    """

    def __init__(self, close_function, disease, world):
        """
        Initializes the information window.

        Parameters:
        ------------
        close_function : function
            Function to call to close the window.
        disease : object
            Instance of the Disease class.
        world : object
            Instance of the World class.
        """
        super().__init__()
        self.controller = InformationsController(disease, world)
        self.close_function = close_function
        self.stats_labels = []
        self.attributes('-alpha', 0.0)
        self.setup()
        self.create_close_button()
        self.create_region_info()
        self.attributes('-alpha', 1.0)

    def create_close_button(self):
        """
        Creates the button to close the information window.
        """
        self.close_button = tk.Button(
            self, text="Close", font=("Courier", 18, "bold"), borderwidth=0,
            highlightthickness=0, pady=10, foreground="red", command=self.open_map)
        self.close_button.grid(
            row=10, column=4, sticky=tk.E, padx=10, pady=10)

    def create_region_info(self):
        """
        Creates and updates the region information.

        The information is periodically updated.
        """
        if not self.stats_labels:
            for i, stat in enumerate(self.controller.get_stats()):
                label_stat = tk.Label(self, text=stat, background="dark grey", font=("Courier", 12))
                label_stat.grid(row=i // 4 + 1, column=i % 4 + 1)
                self.stats_labels.append(label_stat)
        else:
            for i, stat in enumerate(self.controller.get_stats()):
                self.stats_labels[i].configure(text=stat)
        for i in range(6):
            tk.Grid.columnconfigure(self, i, weight=1)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 9, weight=1)
        tk.Grid.rowconfigure(self, 11, weight=1)
        self.after(240, self.create_region_info)

    def open_map(self):
        """
        Closes the information window and returns to the previous window.
        """
        self.close_function()
        self.destroy()

    def setup(self):
        """
        Configures the main information window.
        """
        Global().set_fullscreen(self)
        self.configure(background="dark grey")
        self.title("COVID-24")