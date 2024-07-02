from tkinter import IntVar

class ImprovementsController:
    """
    Controller to manage disease improvements in the graphical interface.

    Attributes:
    -----------
    __disease_model : Disease
        Instance of the Disease class associated with this controller.
    __levels : list
        List containing the levels of different characteristics of the disease as IntVar.
        Indices:
        0: Camouflage level
        1: Infectivity level
        2: Lethality level
        3: Reassembly level
        4: Heat resistance level
        5: Cold resistance level
    __points : IntVar
        Number of upgrade points available.

    Methods:
    ----------
    increase_camouflage()
        Increases the camouflage level of the disease.
    increase_infectivity()
        Increases the infectivity level of the disease.
    increase_lethality()
        Increases the lethality level of the disease.
    increase_reassembly()
        Increases the genetic reassembly level of the disease.
    increase_heat_resistance()
        Increases the heat resistance level of the disease.
    increase_cold_resistance()
        Increases the cold resistance level of the disease.
    get_camouflage(root)
        Returns the camouflage level of the disease as an IntVar.
    get_infectivity(root)
        Returns the infectivity level of the disease as an IntVar.
    get_lethality(root)
        Returns the lethality level of the disease as an IntVar.
    get_reassembly(root)
        Returns the genetic reassembly level of the disease as an IntVar.
    get_heat_resistance(root)
        Returns the heat resistance level of the disease as an IntVar.
    get_cold_resistance(root)
        Returns the cold resistance level of the disease as an IntVar.
    get_points(root)
        Returns the number of available upgrade points as an IntVar.
    """

    __slots__ = ["__disease_model", "__levels", "__points"]

    def __init__(self, disease):
        self.__disease_model = disease
        self.__levels = [IntVar()] * 6
        self.__points = IntVar()

    def increase_camouflage(self):
        """
        Increases the camouflage level of the disease.
        """
        if self.__points.get() - 1 >= 0:
            self.__disease_model.increase_camouflage()
            self.__disease_model.update_points(-1)
            self.__levels[0].set(self.__disease_model.get_camouflage())
            self.__points.set(self.__disease_model.get_points())

    def increase_infectivity(self):
        """
        Increases the infectivity level of the disease.
        """
        if self.__points.get() - 1 >= 0:
            self.__disease_model.increase_infectivity()
            self.__disease_model.update_points(-1)
            self.__levels[1].set(self.__disease_model.get_infectivity())
            self.__points.set(self.__disease_model.get_points())

    def increase_lethality(self):
        """
        Increases the lethality level of the disease.
        """
        if self.__points.get() - 1 >= 0:
            self.__disease_model.increase_lethality()
            self.__disease_model.update_points(-1)
            self.__levels[2].set(self.__disease_model.get_lethality())
            self.__points.set(self.__disease_model.get_points())

    def increase_reassembly(self):
        """
        Increases the genetic reassembly level of the disease.
        """
        if self.__points.get() - 1 >= 0:
            self.__disease_model.increase_reassembly()
            self.__disease_model.update_points(-1)
            self.__levels[3].set(self.__disease_model.get_reassembly())
            self.__points.set(self.__disease_model.get_points())

    def increase_heat_resistance(self):
        """
        Increases the heat resistance level of the disease.
        """
        if self.__points.get() - 1 >= 0:
            self.__disease_model.increase_heat_resistance()
            self.__disease_model.update_points(-1)
            self.__levels[4].set(self.__disease_model.get_heat_resistance())
            self.__points.set(self.__disease_model.get_points())

    def increase_cold_resistance(self):
        """
        Increases the cold resistance level of the disease.
        """
        if self.__points.get() - 1 >= 0:
            self.__disease_model.increase_cold_resistance()
            self.__disease_model.update_points(-1)
            self.__levels[5].set(self.__disease_model.get_cold_resistance())
            self.__points.set(self.__disease_model.get_points())

    def get_camouflage(self, root):
        """
        Returns the camouflage level of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The camouflage level of the disease.
        """
        self.__levels[0] = IntVar(root, self.__disease_model.get_camouflage())
        return self.__levels[0]

    def get_infectivity(self, root):
        """
        Returns the infectivity level of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The infectivity level of the disease.
        """
        self.__levels[1] = IntVar(root, self.__disease_model.get_infectivity())
        return self.__levels[1]

    def get_lethality(self, root):
        """
        Returns the lethality level of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The lethality level of the disease.
        """
        self.__levels[2] = IntVar(root, self.__disease_model.get_lethality())
        return self.__levels[2]

    def get_reassembly(self, root):
        """
        Returns the genetic reassembly level of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The genetic reassembly level of the disease.
        """
        self.__levels[3] = IntVar(root, self.__disease_model.get_reassembly())
        return self.__levels[3]

    def get_heat_resistance(self, root):
        """
        Returns the heat resistance level of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The heat resistance level of the disease.
        """
        self.__levels[4] = IntVar(root, self.__disease_model.get_heat_resistance())
        return self.__levels[4]

    def get_cold_resistance(self, root):
        """
        Returns the cold resistance level of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The cold resistance level of the disease.
        """
        self.__levels[5] = IntVar(root, self.__disease_model.get_cold_resistance())
        return self.__levels[5]

    def get_points(self, root):
        """
        Returns the upgrade points of the disease as an IntVar.

        Parameters:
        ------------
        root : Tk
            The root window of the application.

        Returns:
        ----------
        IntVar :
            The evolution points of the disease.
        """
        self.__points = IntVar(root, self.__disease_model.get_points())
        return self.__points