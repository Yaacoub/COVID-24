import time
from threading import Thread

class Disease:
    """
    Class to manage the characteristics and evolution of a disease.

    Attributes:
    -----------
    __evolution_points : bool
        Indicates if the disease points increase over time.
    __levels : list
        List containing the levels of various characteristics of the disease.
        Indices:
        0 : Camouflage level
        1 : Infectivity level
        2 : Lethality level
        3 : Reassembly level
        4 : Heat resistance level
        5 : Cold resistance level
    __name : str
        Name of the disease.
    __points : int
        Evolution points of the disease.
    __points_thread : threading.Thread
        Thread to automatically increase the disease points.

    Methods:
    --------
    __init__(name):
        Initializes a new instance of the Disease class with the specified name.
    __increase_points():
        Thread that automatically increases the disease points.
    stop_points_growth():
        Stops the automatic increase of points.
    increase_camouflage():
        Increases the camouflage level of the disease.
    increase_infectivity():
        Increases the infectivity level of the disease.
    increase_lethality():
        Increases the lethality level of the disease.
    increase_reassembly():
        Increases the reassembly level of the disease.
    increase_heat_resistance():
        Increases the heat resistance level of the disease.
    increase_cold_resistance():
        Increases the cold resistance level of the disease.
    start_points_growth():
        Starts the automatic increase of points.
    update_points(delta):
        Updates the disease points by a specific value.
    get_camouflage():
        Returns the camouflage level of the disease.
    get_infectivity():
        Returns the infectivity level of the disease.
    get_lethality():
        Returns the lethality level of the disease.
    get_reassembly():
        Returns the reassembly level of the disease.
    get_heat_resistance():
        Returns the heat resistance level of the disease.
    get_cold_resistance():
        Returns the cold resistance level of the disease.
    get_points():
        Returns the points of the disease.
    get_name():
        Returns the name of the disease.
    """

    __slots__ = ["__evolution_points", "__levels", "__name", "__points", "__points_thread"]

    def __init__(self, name):
        """
        Initializes a new instance of the Disease class with the specified name.

        Parameters:
        ------------
        name : str
            The name of the disease.
        """
        super().__init__()
        self.__evolution_points = False
        self.__levels = [1, 1, 1, 1, 1, 1]
        self.__name = name
        self.__points = 0
        self.__points_thread = Thread(target=self.__increase_points, daemon=True)
        self.__points_thread.start()

    def __increase_points(self):
        """
        Thread that automatically increases the disease points every 10 seconds
        if the evolution of points is enabled.
        """
        while True:
            if self.__evolution_points:
                self.__points += 1
                time.sleep(10)

    def stop_points_growth(self):
        """
        Stops the automatic increase of points.
        """
        self.__evolution_points = False

    def increase_camouflage(self):
        """
        Increases the camouflage level of the disease.
        """
        self.__levels[0] += 1

    def increase_infectivity(self):
        """
        Increases the infectivity level of the disease.
        """
        self.__levels[1] += 1

    def increase_lethality(self):
        """
        Increases the lethality level of the disease.
        """
        self.__levels[2] += 1

    def increase_reassembly(self):
        """
        Increases the reassembly level of the disease.
        """
        self.__levels[3] += 1

    def increase_heat_resistance(self):
        """
        Increases the heat resistance level of the disease.
        """
        self.__levels[4] += 1

    def increase_cold_resistance(self):
        """
        Increases the cold resistance level of the disease.
        """
        self.__levels[5] += 1

    def start_points_growth(self):
        """
        Starts the automatic increase of points.
        """
        self.__evolution_points = True

    def update_points(self, delta):
        """
        Updates the disease points by a specific value.

        Parameters:
        ------------
        delta : int
            The value to add to the current points of the disease.
        """
        self.__points += delta

    def get_camouflage(self):
        """
        Returns the camouflage level of the disease.

        Returns:
        ----------
        int:
            The camouflage level of the disease.
        """
        return self.__levels[0]

    def get_infectivity(self):
        """
        Returns the infectivity level of the disease.

        Returns:
        ----------
        int:
            The infectivity level of the disease.
        """
        return self.__levels[1]

    def get_lethality(self):
        """
        Returns the lethality level of the disease.

        Returns:
        ----------
        int:
            The lethality level of the disease.
        """
        return self.__levels[2]

    def get_reassembly(self):
        """
        Returns the reassembly level of the disease.

        Returns:
        ----------
        int:
            The reassembly level of the disease.
        """
        return self.__levels[3]

    def get_heat_resistance(self):
        """
        Returns the heat resistance level of the disease.

        Returns:
        ----------
        int:
            The heat resistance level of the disease.
        """
        return self.__levels[4]

    def get_cold_resistance(self):
        """
        Returns the cold resistance level of the disease.

        Returns:
        ----------
        int:
            The cold resistance level of the disease.
        """
        return self.__levels[5]

    def get_points(self):
        """
        Returns the points of the disease.

        Returns:
        ----------
        int:
            The evolution points of the disease.
        """
        return self.__points

    def get_name(self):
        """
        Returns the name of the disease.

        Returns:
        ----------
        str:
            The name of the disease.
        """
        return self.__name