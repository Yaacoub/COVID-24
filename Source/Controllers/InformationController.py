class InformationController:
    """
    Controller to manage information regarding the disease and region statistics.

    Attributes:
    -----------
    __disease_model : Disease
        Instance of the Disease class managed by this controller.
    __world_model : World
        Instance of the World class containing the regions and their statistics.

    Methods:
    ----------
    __init__(self, disease, world):
        Initializes a new instance of the controller with the specified disease and world.

    get_disease_name(self):
        Returns the name of the disease managed by this controller.

    get_stats(self):
        Returns a list of statistics for each region in the world.
    """

    __slots__ = ["__disease_model", "__world_model"]

    def __init__(self, disease, world):
        """
        Initializes a new instance of the controller with the specified disease and world.

        Parameters:
        ------------
        disease : Disease
            Instance of the Disease class to manage.
        world : World
            Instance of the World class containing the regions and their statistics.
        """
        self.__disease_model = disease
        self.__world_model = world

    def get_disease_name(self):
        """
        Returns the name of the disease managed by this controller.

        Returns:
        ----------
        str :
            The name of the disease.
        """
        return self.__disease_model.get_name()

    def get_stats(self):
        """
        Returns a list of statistics for each region in the world.

        Each statistic includes the name of the region, the initial population,
        and the healthy, recovered, infected, and dead populations.

        Returns:
        ----------
        list of str :
            A list of strings containing the statistics of each region.
        """
        stats = []
        for region in self.__world_model.get_regions():
            stat = f"{region.get_name()}\n"
            stat += f"{region.get_initial_population():.2f} M\n\n"
            stat += f"Healthy: {region.get_healthy_population():.2f} M\n"
            stat += f"Recovered: {region.get_recovered_population():.2f} M\n"
            stat += f"Infected: {region.get_infected_population():.2f} M\n"
            stat += f"Dead: {region.get_dead_population():.2f} M\n\n"
            stats.append(stat)
        return stats