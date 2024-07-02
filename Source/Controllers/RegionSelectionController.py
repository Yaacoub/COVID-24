from Source.Modeles.Monde import Monde

class RegionSelectionController:
    """
    Controller to manage region selection and interactions with the disease and world models.

    Attributes:
    -----------
    __disease_model : Disease
        Model representing the disease.
    __world_model : World
        Model representing the world and its regions.

    Methods:
    --------
    __init__(self, disease):
        Initializes a new instance of the region selection controller with the specified disease.

    select_region(self, name):
        Initializes the infected population of the specified region by name.

    get_disease(self):
        Returns the disease model.

    get_world(self):
        Returns the world model.

    get_regions(self):
        Returns a list of the names of all regions.
    """

    __slots__ = ["__disease_model", "__world_model"]

    def __init__(self, disease):
        """
        Initializes a new instance of the region selection controller with the specified disease.

        Parameters:
        ------------
        disease : Disease
            The model representing the disease.
        """
        self.__disease_model = disease
        self.__world_model = Monde()

    def select_region(self, name):
        """
        Initializes the infected population of the specified region by name.

        Parameters:
        ------------
        name : str
            The name of the region to infect.
        """
        for region in self.__world_model.get_regions():
            if region.get_name() == name:
                self.__world_model.init_infected_pop(name)
                break

    def get_disease(self):
        """
        Returns the disease model.

        Returns:
        ----------
        Disease :
            The model representing the disease.
        """
        return self.__disease_model

    def get_world(self):
        """
        Returns the world model.

        Returns:
        ----------
        World :
            The model representing the world and its regions.
        """
        return self.__world_model

    def get_regions(self):
        """
        Returns a list of the names of all regions.

        Returns:
        ----------
        list :
            A list of strings representing the names of the regions.
        """
        names = [region.get_name() for region in self.__world_model.get_regions()]
        return names