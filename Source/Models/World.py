import csv
import os
from Source.Models.Region import Region

class World:
    """
    Class to manage the different regions of the world.

    Attributes:
    -----------
    __regions : dict
        Dictionary containing the world's regions with their name as the key
        and the corresponding Region object as the value.

    Methods:
    --------
    __init__():
        Initializes a new instance of the World class by retrieving region data.
    __retrieve_regions():
        Retrieves region data from CSV files.
    initialize_infected_population(region_name):
        Initializes the infected population for a specific region.
    get_regions():
        Returns the list of Region objects representing the world's regions.
    """

    __slots__ = ["__regions"]

    def __init__(self):
        """
        Initializes a new instance of the World class by retrieving region data.
        """
        self.__regions = {}
        self.__retrieve_regions()

    def __retrieve_regions(self):
        """
        Retrieves region data from CSV files.
        """
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

        file_path = os.path.join(root, "Data", "Population.csv")
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                name = row[0]
                population = row[1].replace("\u202f", "")
                region = Region(name)
                region.set_healthy_population(float(population))
                self.__regions[name] = region

        file_path = os.path.join(root, "Data", "Area.csv")
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                name = row[0]
                area = row[1]
                region = self.__regions[name]
                region.set_area(float(area))

        file_path = os.path.join(root, "Data", "Temperature.csv")
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                name = row[0]
                temperature = row[1]
                region = self.__regions[name]
                region.set_temperature(float(temperature))

        file_path = os.path.join(root, "Data", "Neighborhood.csv")
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=":")
            next(reader)
            for row in reader:
                name = row[0]
                neighbors = [self.__regions[neighbor_name] for neighbor_name in row[1].split(",")]
                region = self.__regions[name]
                region.set_neighbors(neighbors)

        del self.__regions["World"]

    def initialize_infected_population(self, region_name):
        """
        Initializes the infected population for a specific region.

        Parameters:
        ------------
        region_name : str
            The name of the region to initialize.
        """
        self.__regions[region_name].set_infected_population(0.01)

    def get_regions(self):
        """
        Returns the list of Region objects representing the world's regions.

        Returns:
        ----------
        list :
            List of Region objects.
        """
        return list(self.__regions.values())