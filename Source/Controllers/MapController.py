import os
import random
import time
from datetime import date
from threading import Thread
from Source.Modeles.Actualites import Actualites

class MapController:
    """
    Controller to manage interactions and the evolution of regions in the world.

    This class handles the evolution of populations, the management of news, 
    and interaction with the disease and world models.

    Attributes:
    -----------
    __cursor_index : int
        Index for scrolling news.
    __disease_model : Disease
        Model representing the disease.
    __news_model : News
        Model for managing news and the date.
    __world_model : World
        Model representing the world and its regions.
    __evolution_thread : Thread
        Thread to manage population evolution asynchronously.

    Methods:
    --------
    __init__(self, disease, world):
        Initializes a new instance of the map controller with the specified 
        disease and world.

    __euler(self):
        Performs an iteration of the evolution algorithm based on the Euler 
        method for each region.

    __evolve_populations(self):
        Manages the evolution of populations in all regions continuously.

    __infect_neighbors(self):
        Spreads the infection to neighboring regions based on specified 
        conditions.

    __get_rates(self, region):
        Calculates the rates of populations (infected, dead, recovered, healthy) 
        for a given region.

    stop_growth_points(self):
        Stops the growth of disease points.

    start_growth_points(self):
        Starts the growth of disease points.

    get_map_paths(self):
        Returns the paths of image files representing the maps of regions and 
        the world.

    get_colors(self):
        Returns the colors representing the state of the regions.

    get_date(self):
        Returns the current date from the news model and increments by one day.

    get_disease(self):
        Returns the disease model.

    get_world(self):
        Returns the world model.

    get_disease_name(self):
        Returns the name of the disease.

    get_scrolled_news(self):
        Returns the scrolled news from the news model.

    get_region_tags(self):
        Returns the names of regions for labeling.

    get_world_rates(self):
        Calculates the rates of populations (infected, dead, recovered, healthy) 
        for the entire world.
    """

    __slots__ = ["__cursor_index", "__disease_model", "__news_model", "__world_model",
                 "__evolution_thread"]

    def __init__(self, disease, world):
        """
        Initializes a new instance of the map controller with the specified disease and world.
        
        Parameters:
        ------------
        disease : Disease
            The disease model.
        world : World
            The world model.
        """
        today = date.today()
        current_date = date(year=1960, month=today.month, day=today.day)
        self.__cursor_index = 0
        self.__news_model = Actualites(current_date)
        self.__disease_model = disease
        self.__world_model = world
        self.__evolution_thread = Thread(target=self.__evolve_populations, daemon=True)
        self.__evolution_thread.start()

    def __euler(self):
        """
        Performs an iteration of the evolution algorithm based on the Euler method.
        """
        dt = 0.1
        for region in self.__world_model.get_regions():

            # Levels
            levels = [self.__disease_model.get_camouflage(),
                      self.__disease_model.get_infectivity(),
                      self.__disease_model.get_lethality(),
                      self.__disease_model.get_reassembly(),
                      self.__disease_model.get_heat_resistance(),
                      self.__disease_model.get_cold_resistance()]

            # Populations
            s = region.get_healthy_pop()
            i = region.get_infected_pop()
            r = region.get_recovered_pop()
            m = region.get_dead_pop()

            # Probabilities
            b = s / region.get_area() * levels[1]
            g = 1 / levels[0] + 1 / levels[3]
            d = levels[2]

            g += 1 / levels[5] if region.get_temperature() < 20 else 1 / levels[4]
            b *= 1
            g *= 1e-6
            d *= 1e-6

            print(region.get_name(), b, g, d)

            t = 0
            while t < 10:
                t += dt
                s += dt * (-b * s * i)
                i += dt * (b * s * i - g * i - d * i)
                r += dt * (g * i)
                m += dt * (d * i)

            region.modify_healthy_pop(s)
            region.modify_infected_pop(i)
            region.modify_recovered_pop(r)
            region.modify_dead_pop(m)

    def __evolve_populations(self):
        """
        Manages the evolution of populations in all regions continuously.
        """
        a = 0
        while True:
            self.__euler()
            a += 1
            if a % 4 == 0:
                a = 0
                self.__infect_neighbors()
            time.sleep(0.240)

    def __infect_neighbors(self):
        """
        Spreads the infection to neighboring regions based on specified conditions.
        """
        for region in self.__world_model.get_regions():
            if region.get_infected_pop() / region.get_initial_pop() >= 0.1:
                if region.get_infected_pop() == 0 and random.randint(0, 99) == 1:
                    self.__world_model.init_infected_pop(region.get_name())
                else:
                    neighbor = random.choice(region.get_neighbors())
                    if neighbor.get_infected_pop() == 0:
                        self.__world_model.init_infected_pop(neighbor.get_name())

    def __get_rates(self, region):
        """
        Calculates the rates of populations (infected, dead, recovered, healthy) for a given region.

        Parameters:
        ------------
        region : Region
            The region for which the rates are calculated.

        Returns:
        ----------
        tuple :
            A tuple containing the rates of infection, mortality, recovery, and health.
        """
        infected = 0
        dead = 0
        recovered = 0
        healthy = 0
        infected_pop = region.get_infected_pop()
        dead_pop = region.get_dead_pop()
        recovered_pop = region.get_recovered_pop()
        healthy_pop = region.get_healthy_pop()
        population = infected_pop + dead_pop + recovered_pop + healthy_pop
        infected = infected_pop / population
        dead = dead_pop / population
        recovered = recovered_pop / population
        healthy = healthy_pop / population
        return (infected, dead, recovered, healthy)

    def stop_growth_points(self):
        """
        Stops the growth of disease points.
        """
        self.__disease_model.stop_growth_points()

    def start_growth_points(self):
        """
        Starts the growth of disease points.
        """
        self.__disease_model.start_growth_points()

    def get_map_paths(self):
        """
        Returns the paths of image files representing the maps of regions and the world.

        Returns:
        ----------
        list :
            A list of paths to the image files of the maps.
        """
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        map_paths = [region.get_map_path()
                     for region in self.__world_model.get_regions()]
        world_map_path = os.path.join(root, "Assets", "Maps", "world.png")
        return [world_map_path] + map_paths

    def get_colors(self):
        """
        Returns the colors representing the state of the regions.

        Returns:
        ----------
        list :
            A list of colors for each region.
        """
        result = []
        for region in self.__world_model.get_regions():
            rates = self.__get_rates(region)
            r = rates[0] * 255 + rates[1] * 255
            g = 0
            b = rates[1] * 255
            result.append([r, g, b])
        return result

    def get_date(self):
        """
        Returns the current date from the news model and increments by one day.

        Returns:
        ----------
        str :
            The current date as a string.
        """
        date_string = self.__news_model.get_date()
        self.__news_model.add_day()
        return date_string

    def get_disease(self):
        """
        Returns the disease model.

        Returns:
        ----------
        Disease :
            The disease model.
        """
        return self.__disease_model

    def get_world(self):
        """
        Returns the world model.

        Returns:
        ----------
        World :
            The world model.
        """
        return self.__world_model

    def get_disease_name(self):
        """
        Returns the name of the disease.

        Returns:
        ----------
        str :
            The name of the disease.
        """
        return self.__disease_model.get_name()

    def get_scrolled_news(self):
        """
        Returns the scrolled news from the news model.

        Returns:
        ----------
        str :
            The scrolled news as a string.
        """
        text = self.__news_model.get_news()
        text_label = text[self.__cursor_index:] + \
            text[:self.__cursor_index]
        if self.__cursor_index < len(text) - 1:
            self.__cursor_index += 1
        else:
            self.__cursor_index = 0
        return text_label

    def get_region_tags(self):
        """
        Returns the names of regions for labeling.

        Returns:
        ----------
        list :
            A list of region names.
        """
        map_paths = [region.get_name()
                     for region in self.__world_model.get_regions()]
        world_map_path = map_paths.pop()
        return [world_map_path] + map_paths

    def get_world_rates(self):
        """
        Calculates the rates of populations (infected, dead, recovered, healthy) for the entire world.

        Returns:
        ----------
        list :
            A list of infection, mortality, recovery, and health rates for the world.
        """
        infected_pop = 0
        dead_pop = 0
        recovered_pop = 0
        healthy_pop = 0
        population = 0
        for region in list(self.__world_model.get_regions()):
            infected_pop += region.get_infected_pop()
            dead_pop += region.get_dead_pop()
            recovered_pop += region.get_recovered_pop()
            healthy_pop += region.get_healthy_pop()
            population += region.get_initial_pop()
        return [infected_pop / population * 100,
                dead_pop / population * 100,
                recovered_pop / population * 100,
                healthy_pop / population * 100]