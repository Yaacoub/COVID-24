import tkinter as tk
from Source.Global import Global
from Source.Controllers.ImprovementsController import ImprovementsController

class Improvements(tk.Tk):
    """
    Class representing the improvements window of the COVID-24 application.

    Inherits from:
    --------------
    tk.Tk : Base class for creating Tkinter windows.

    Attributes:
    -----------
    controller : ImprovementsController
        Controller to manage disease improvements.
    close_callback : function
        Callback function to handle window closure.

    Methods:
    --------
    __init__(self, close_callback, disease):
        Initializes the improvements window and configures its elements.
        
    create_buttons(self):
        Creates and places the improvement buttons in the window.
        
    create_points_labels(self):
        Creates and places the labels displaying points and improvement levels.
        
    create_title_labels(self):
        Creates and places the labels for improvement titles.
        
    open_map(self):
        Closes the current window and opens the map.
        
    setup(self):
        Configures the window for fullscreen display and sets the title and background.
    """

    def __init__(self, close_callback, disease):
        """
        Initializes the improvements window and configures its elements.

        Parameters:
        ------------
        close_callback : function
            Callback function to handle window closure.
        disease : object
            Instance of the Disease class.
        """
        super().__init__()
        self.controller = ImprovementsController(disease)
        self.close_callback = close_callback
        self.attributes('-alpha', 0.0)
        self.setup()
        self.create_title_labels()
        self.create_buttons()
        self.create_points_labels()
        self.attributes('-alpha', 1.0)

    def create_buttons(self):
        """
        Creates and places the improvement buttons in the window.
        """
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 10, weight=1)
        tk.Grid.rowconfigure(self, 12, weight=1)

        self.button_lethality = tk.Button(
            self, text="+", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, command=self.controller.increase_lethality)
        self.button_lethality.grid(row=1, column=2, sticky=tk.W, padx=10, pady=10)

        self.button_infectivity = tk.Button(
            self, text="+", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, command=self.controller.increase_infectivity)
        self.button_infectivity.grid(row=2, column=2, sticky=tk.W, padx=10, pady=10)

        self.button_camouflage = tk.Button(
            self, text="+", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, command=self.controller.increase_camouflage)
        self.button_camouflage.grid(row=3, column=2, sticky=tk.W, padx=10, pady=10)

        self.button_reassembly = tk.Button(
            self, text="+", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, command=self.controller.increase_reassembly)
        self.button_reassembly.grid(row=4, column=2, sticky=tk.W, padx=10, pady=10)

        self.button_heat_resistance = tk.Button(
            self, text="+", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, command=self.controller.increase_heat_resistance)
        self.button_heat_resistance.grid(row=5, column=2, sticky=tk.W, padx=10, pady=10)

        self.button_cold_resistance = tk.Button(
            self, text="+", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, command=self.controller.increase_cold_resistance)
        self.button_cold_resistance.grid(row=6, column=2, sticky=tk.W, padx=10, pady=10)

        self.button_close = tk.Button(
            self, text="Close", font=("Courier", 18, "bold"), borderwidth=0, highlightthickness=0,
            pady=10, foreground="red", command=self.open_map)
        self.button_close.grid(row=11, column=3, sticky=tk.E, padx=10, pady=10)

    def create_points_labels(self):
        """
        Creates and places the labels displaying points and improvement levels.
        """
        self.label_lethality_level = tk.Label(
            self, textvariable=self.controller.get_lethality(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_lethality_level.grid(row=1, column=3, sticky=tk.W, padx=10, pady=10)

        self.label_infectivity_level = tk.Label(
            self, textvariable=self.controller.get_infectivity(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_infectivity_level.grid(row=2, column=3, sticky=tk.W, padx=10, pady=10)

        self.label_camouflage_level = tk.Label(
            self, textvariable=self.controller.get_camouflage(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_camouflage_level.grid(row=3, column=3, sticky=tk.W, padx=10, pady=10)

        self.label_reassembly_level = tk.Label(
            self, textvariable=self.controller.get_reassembly(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_reassembly_level.grid(row=4, column=3, sticky=tk.W, padx=10, pady=10)

        self.label_heat_resistance_level = tk.Label(
            self, textvariable=self.controller.get_heat_resistance(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_heat_resistance_level.grid(row=5, column=3, sticky=tk.W, padx=10, pady=10)

        self.label_cold_resistance_level = tk.Label(
            self, textvariable=self.controller.get_cold_resistance(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_cold_resistance_level.grid(row=6, column=3, sticky=tk.W, padx=10, pady=10)

        self.label_points = tk.Label(
            self, textvariable=self.controller.get_points(self),
            font=("Courier", 18, "bold"), background="dark grey", foreground="red2", pady=10)
        self.label_points.grid(row=7, column=3, sticky=tk.W, padx=10, pady=10)

    def create_title_labels(self):
        """
        Creates and places the labels for improvement titles.
        """
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 4, weight=1)

        self.label_lethality = tk.Label(
            self, text="Lethality", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_lethality.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

        self.label_infectivity = tk.Label(
            self, text="Infectivity", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_infectivity.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        self.label_camouflage = tk.Label(
            self, text="Camouflage", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_camouflage.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        self.label_reassembly = tk.Label(
            self, text="Genetic Reassembly", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_reassembly.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        self.label_heat_resistance = tk.Label(
            self, text="Heat Resistance", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_heat_resistance.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

        self.label_cold_resistance = tk.Label(
            self, text="Cold Resistance", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_cold_resistance.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)

        self.label_points = tk.Label(
            self, text="Points", font=("Courier", 18, "bold"),
            background="dark grey", pady=10)
        self.label_points.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

    def open_map(self):
        """
        Closes the current window and opens the map.
        """
        self.close_callback()
        self.destroy()

    def setup(self):
        """
        Configures the window for fullscreen display and sets the
        title and background.
        """
        Global().set_fullscreen(self)
        self.configure(background="dark grey")
        self.title("COVID-24")