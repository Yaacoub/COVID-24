import csv
import os
from datetime import timedelta

class News:
    """
    Class to manage news on a specific date.

    Attributes:
    -----------
    __date : datetime
        The date of the news.
    __news : list
        The list of news for the given date.

    Methods:
    --------
    __init__(date):
        Initializes a new instance of the News class with the specified date.
    __initialize_news():
        Initializes the news by reading the CSV file.
    add_day():
        Adds a day to the current date.
    add_news_item(news_item):
        Adds a news item to the list of news.
    get_date():
        Returns the date as a formatted string.
    get_news():
        Returns the news as a string with spaces for each news item.
    """

    __slots__ = ["__date", "__news"]

    def __init__(self, date):
        """
        Initializes a new instance of the News class with the specified date.

        Parameters:
        ------------
        date : datetime
            The initial date of the news.
        """
        super().__init__()
        self.__date = date
        self.__news = []
        self.__initialize_news()

    def __initialize_news(self):
        """
        Initializes the news by reading the CSV file located in the 'Data' directory.
        """
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        file = os.path.join(root, "Data", "News.csv")

        with open(file, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            next(reader)
            for line in reader:
                self.__news.append(line[0])

    def add_day(self):
        """
        Adds a day to the current date.
        """
        self.__date += timedelta(days=1)

    def add_news_item(self, news_item):
        """
        Adds a news item to the list of news.
        If the list exceeds 4 items, the oldest one is removed.

        Parameters:
        ------------
        news_item : str
            The news item to add to the list.
        """
        self.__news.append(news_item)
        if len(self.__news) > 4:
            self.__news.pop(0)

    def get_date(self):
        """
        Returns the date as a formatted string.

        Returns:
        ----------
        str:
            The date formatted as a string.
        """
        return self.__date.strftime("%d %b %Y")

    def get_news(self):
        """
        Returns the news as a string with spaces for each news item.

        Returns:
        ----------
        str:
            The news as a string with spaces for each news item.
        """
        space = " " * 10
        return space + space.join(self.__news)