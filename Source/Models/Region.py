import os

class Region:
    """
    Class representing a region.

    Attributes:
    -----------
    __name : str
        Name of the region.
    __map_path : str
        Path to the image file representing the map of the region.
    __population : list
        List containing population information of the region.
        Indices:
        0: Infected population
        1: Deceased population
        2: Recovered population
        3: Healthy population
    __area : float
        Area of the region.
    __temperature : float
        Temperature of the region.
    __neighbors : list
        List of neighboring regions.

    Methods:
    --------
    __init__(name):
        Initializes a new instance of the Region class with the specified name.
    __initialize_map():
        Initializes the path to the image file representing the map of the region.
    set_healthy_population(value):
        Sets the healthy population of the region.
    set_infected_population(value):
        Sets the infected population of the region.
    set_deceased_population(value):
        Sets the deceased population of the region.
    set_recovered_population(value):
        Sets the recovered population of the region.
    set_area(value):
        Sets the area of the region.
    set_temperature(value):
        Sets the temperature of the region.
    set_neighbors(value):
        Sets the list of neighboring regions.
    get_map_path():
        Returns the path to the image file representing the map of the region.
    get_name():
        Returns the name of the region.
    get_infected_population():
        Returns the infected population of the region.
    get_initial_population():
        Returns the total population (infected, deceased, recovered, healthy) of the region.
    get_deceased_population():
        Returns the deceased population of the region.
    get_recovered_population():
        Returns the recovered population of the region.
    get_healthy_population():
        Returns the healthy population of the region.
    get_area():
        Returns the area of the region.
    get_temperature():
        Returns the temperature of the region.
    get_neighbors():
        Returns the list of neighboring regions.
    """

    __slots__ = ["__name", "__map_path", "__population", "__area", "__temperature", "__neighbors"]

    def __init__(self, name):
        """
        Initializes a new instance of the Region class with the specified name.

        Parameters:
        ------------
        name : str
            The name of the region.
        """
        self.__name = name
        self.__population = [0, 0, 0, 0]
        self.__area = 0
        self.__temperature = 0
        self.__neighbors = []
        self.__initialize_map()

    def __initialize_map(self):
        """
        Initializes the path to the image file representing the map of the region.
        """
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        file_path = os.path.join(root, "Assets", "Maps", f"{self.__name.lower()}.png")
        self.__map_path = file_path

    def set_infected_population(self, value):
        """
        Sets the infected population of the region.

        Parameters:
        ------------
        value : float
            The new value of the infected population.
        """
        self.__population[0] = value

    def set_deceased_population(self, value):
        """
        Sets the deceased population of the region.

        Parameters:
        ------------
        value : float
            The new value of the deceased population.
        """
        self.__population[1] = value

    def set_recovered_population(self, value):
        """
        Sets the recovered population of the region.

        Parameters:
        ------------
        value : float
            The new value of the recovered population.
        """
        self.__population[2] = value

    def set_healthy_population(self, value):
        """
        Sets the healthy population of the region.

        Parameters:
        ------------
        value : float
            The new value of the healthy population.
        """
        self.__population[3] = value

    def set_area(self, value):
        """
        Sets the area of the region.

        Parameters:
        ------------
        value : float
            The new value of the area.
        """
        self.__area = value

    def set_temperature(self, value):
        """
        Sets the temperature of the region.

        Parameters:
        ------------
        value : float
            The new value of the temperature.
        """
        self.__temperature = value

    def set_neighbors(self, value):
        """
        Sets the list of neighboring regions.

        Parameters:
        ------------
        value : list
            The new list of neighboring regions.
        """
        self.__neighbors = value

    def get_map_path(self):
        """
        Returns the path to the image file representing the map of the region.

        Returns:
        ----------
        str :
            The path to the image file.
        """
        return self.__map_path

    def get_name(self):
        """
        Returns the name of the region.

        Returns:
        ----------
        str :
            The name of the region.
        """
        return self.__name

    def get_infected_population(self):
        """
        Returns the infected population of the region.

        Returns:
        ----------
        float :
            The infected population of the region.
        """
        return self.__population[0]

    def get_initial_population(self):
        """
        Returns the total population (infected, deceased, recovered, healthy) of the region.

        Returns:
        ----------
        float :
            The total population of the region.
        """
        return sum(self.__population)

    def get_deceased_population(self):
        """
        Returns the deceased population of the region.

        Returns:
        ----------
        float :
            The deceased population of the region.
        """
        return self.__population[1]

    def get_recovered_population(self):
        """
        Returns the recovered population of the region.

        Returns:
        ----------
        float :
            The recovered population of the region.
        """
        return self.__population[2]

    def get_healthy_population(self):
        """
        Returns the healthy population of the region.

        Returns:
        ----------
        float :
            The healthy population of the region.
        """
        return self.__population[3]

    def get_area(self):
        """
        Returns the area of the region.

        Returns:
        ----------
        float :
            The area of the region.
        """
        return self.__area

    def get_temperature(self):
        """
        Returns the temperature of the region.

        Returns:
        ----------
        float :
            The temperature of the region.
        """
        return self.__temperature

    def get_neighbors(self):
        """
        Returns the list of neighboring regions.

        Returns:
        ----------
        list :
            The list of neighboring regions.
        """
        return self.__neighbors