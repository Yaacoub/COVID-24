from Source.Modeles.Maladie import Maladie

class DiseaseCreationController:
    """
    Controller to manage the creation and access of a disease.

    Attributes:
    -----------
    __disease_model : Disease
        Instance of the Disease class created by this controller.

    Methods:
    ----------
    __init__(self):
        Initializes a new instance of the disease creation controller.

    create_disease(self, name):
        Creates a new instance of Disease with the specified name.

    get_disease(self):
        Returns the created instance of Disease.
    """

    __slots__ = ["__disease_model"]

    def __init__(self):
        """
        Initializes a new instance of the disease creation controller.
        """
        self.__disease_model = None

    def create_disease(self, name):
        """
        Creates a new instance of Disease with the specified name.

        Parameters:
        ------------
        name : str
            The name of the disease to create.
        """
        self.__disease_model = Maladie(name)

    def get_disease(self):
        """
        Returns the created instance of Disease.

        Returns:
        ----------
        Disease :
            The instance of the Disease class created by this controller,
            or None if no disease has been created.
        """
        return self.__disease_model