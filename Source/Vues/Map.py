import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from Source.Global import Global
from Source.Controllers.MapController import MapController
from Source.Views.Improvements import Improvements
from Source.Views.Information import Information

class Map(tk.Tk):
    """
    Class representing the main game window.

    Inherits from tk.Tk and uses the PIL and NumPy libraries to manage
    the display of maps and game information.

    Attributes:
    -----------
    controller : MapController
        Instance of MapController to manage interactions and data.
    map_paths : list
        List of paths to world map images.
    image : PIL.Image.Image
        Combined image of the world maps.
    photo : PIL.ImageTk.PhotoImage
        Image displayed in the canvas of the window.

    Methods:
    --------
    __init__(disease, world):
        Initializes the map window with the given disease and world.
    create_improvements_button():
        Creates the button to open the improvements window.
    create_information_button():
        Creates the button to open the information window.
    create_quit_button():
        Creates the button to quit the game.
    create_canvas():
        Creates the canvas to display the game maps.
    create_maps():
        Creates and displays the game maps.
    create_date():
        Creates the date display in the window.
    create_info_labels():
        Creates the information labels in the window.
    create_disease_name():
        Creates the display of the disease name in the window.
    create_ticker():
        Creates the scrolling ticker at the top of the window.
    scroll_date():
        Updates the date display in the window.
    scroll_ticker():
        Scrolls the news in the ticker at the top of the window.
    child_window_close():
        Reactivates the parent window when the child window is closed.
    update_rates():
        Updates the infection, mortality, recovery, and healthy population rates.
    open_improvements():
        Opens the improvements window and pauses point growth.
    open_information():
        Opens the information window and pauses point growth.
    quit_game():
        Closes the game window and stops the program.
    setup():
        Configures the main game window.
    """

    def __init__(self, disease, world):
        """
        Initializes the map window.

        Parameters:
        ------------
        disease : object
            Instance of the Disease class.
        world : object
            Instance of the World class.
        """
        super().__init__()
        self.controller = MapController(disease, world)
        self.map_paths = self.controller.get_map_paths()
        self.image = None
        self.photo = None
        self.attributes('-alpha', 0.0)
        self.setup()
        self.create_improvements_button()
        self.create_information_button()
        self.create_quit_button()
        self.create_canvas()
        self.create_date()
        self.create_info_labels()
        self.create_disease_name()
        self.create_ticker()
        self.after(0, self.attributes, "-alpha", 1.0)
        self.after(10, self.create_maps)

    def create_improvements_button(self):
        """
        Creates the button to open the improvements window.
        """
        self.improvements_button = tk.Button(
            self, text="Improvements", font=("Courier", 18, "bold"),
            borderwidth=0, highlightthickness=0, pady=10, command=self.open_improvements)
        self.improvements_button.grid(column=0, row=2, sticky=tk.NSEW)

    def create_information_button(self):
        """
        Creates the button to open the information window.
        """
        self.information_button = tk.Button(
            self, text="Information", font=("Courier", 18, "bold"),
            borderwidth=0, highlightthickness=0, pady=10, command=self.open_information)
        self.information_button.grid(column=6, row=2, sticky=tk.NSEW)

    def create_quit_button(self):
        """
        Creates the button to quit the game.
        """
        self.quit_button = tk.Button(
            self, text="Quit", font=("Courier", 18, "bold"),
            borderwidth=0, highlightthickness=0, pady=10, command=self.quit_game)
        self.quit_button.grid(column=0, row=0, sticky=tk.NSEW)

    def create_canvas(self):
        """
        Creates the canvas to display the game maps.
        """
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)
        self.canvas = tk.Canvas(self, background="black", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=7, sticky=tk.NSEW)

    def create_maps(self):
        """
        Creates and displays the game maps.
        """
        if self.winfo_viewable():
            width = self.winfo_width()
            height = self.winfo_height()
            colors = self.controller.get_colors()
            self.image = None

            for i, path in enumerate(self.map_paths):
                image = Image.open(path).convert("RGBA")
                if i != 0:
                    array = np.array(image)
                    array[..., 0:3] = colors[i - 1]
                    array[..., 3] = 0.5 * 255 * (array[..., 3] != 0)
                    image = Image.fromarray(array)
                if self.image is None:
                    self.image = image
                else:
                    self.image.paste(image, (0, 0), image)

            self.photo = ImageTk.PhotoImage(self.image.resize((width, height)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.after(10000, self.create_maps)

    def create_date(self):
        """
        Creates the date display in the window.
        """
        self.date_label = tk.Label(
            self, foreground="red2", font=("Courier", 18), padx=10, pady=10)
        self.date_label.grid(column=6, row=0, sticky=tk.NSEW)
        self.scroll_date()

    def create_info_labels(self):
        """
        Creates the information labels in the window.
        """
        self.infected_label = tk.Label(
            self, text="Infected", background="black", foreground="red",
            font=("Courier", 18, "bold"), padx=80, pady=10)
        self.infected_label.grid(column=4, row=2, sticky=tk.NW)

        self.dead_label = tk.Label(
            self, text="Dead", background="black", foreground="magenta3",
            font=("Courier", 18, "bold"), padx=80, pady=10)
        self.dead_label.grid(column=5, row=2, sticky=tk.NW)

        self.recovered_label = tk.Label(
            self, text="Recovered", background="black", foreground="green",
            font=("Courier", 18, "bold"), padx=80, pady=10)
        self.recovered_label.grid(column=2, row=2, sticky=tk.NW)

        self.healthy_label = tk.Label(
            self, text="Healthy", background="black", foreground="royalblue",
            font=("Courier", 18, "bold"), padx=80, pady=10)
        self.healthy_label.grid(column=1, row=2, sticky=tk.NW)

        self.update_rates()

    def create_disease_name(self):
        """
        Creates the display of the disease name in the window.
        """
        self.disease_name_label = tk.Label(
            self, text=self.controller.get_disease_name(), background="black",
            foreground="white", font=("Courier", 18, "bold"), padx=80, pady=10)
        self.disease_name_label.grid(column=3, row=2)

    def create_ticker(self):
        """
        Creates the scrolling ticker at the top of the window.
        """
        self.ticker_label = tk.Label(
            self, background="red2", font=("Courier", 18), pady=10, justify=tk.LEFT, anchor=tk.W)
        self.ticker_label.grid(column=1, row=0, columnspan=5, sticky=tk.NSEW)
        self.scroll_ticker()

    def scroll_date(self):
        """
        Updates the date display in the window.
        """
        self.date_label.configure(text=self.controller.get_date())
        self.after(240, self.scroll_date)

    def scroll_ticker(self):
        """
        Scrolls the news in the ticker at the top of the window.
        """
        text = self.controller.get_scrolling_news()
        self.ticker_label.configure(text=text)
        self.after(120, self.scroll_ticker)

    def child_window_close(self):
        """
        Reactivates the parent window when the child window is closed.
        """
        self.deiconify()
        self.setup()

    def update_rates(self):
        """
        Updates the infection, mortality, recovery, and healthy population rates.
        """
        rates = self.controller.get_world_rates()
        self.infected_label.config(text=f"Infected\n{rates[0]:.2f}%")
        self.dead_label.config(text=f"Dead\n{rates[1]:.2f}%")
        self.recovered_label.config(text=f"Recovered\n{rates[2]:.2f}%")
        self.healthy_label.config(text=f"Healthy\n{rates[3]:.2f}%")
        self.after(1000, self.update_rates)

    def open_improvements(self):
        """
        Opens the improvements window and pauses point growth.
        """
        close = self.child_window_close
        disease = self.controller.get_disease()
        self.controller.stop_point_growth()
        _ = Improvements(close, disease)
       

 self.withdraw()

    def open_information(self):
        """
        Opens the information window and pauses point growth.
        """
        close = self.child_window_close
        disease = self.controller.get_disease()
        world = self.controller.get_world()
        self.controller.stop_point_growth()
        _ = Information(close, disease, world)
        self.withdraw()

    def quit_game(self):
        """
        Closes the game window and stops the program.
        """
        self.destroy()

    def setup(self):
        """
        Configures the main game window.
        """
        Global().set_fullscreen(self)
        self.configure(background="black")
        self.title("COVID-24")
        self.controller.start_point_growth()