import random
import datetime


class Movies:
    def __init__(self):
        """
        Constructor method to create new movie records with a randomly generated ID, title, year, genre and release date.
        """
        self.id = random.randint(1, 10000)
        self.title = None
        self.year = None
        self.genre = None
        self.release_date = None

    def set_title(self, title):
        """
        Method to set the title of the movie.
        """
        self.title = title

    def set_year(self, year):
        """
        Method to set the release year of the movie.
        """
        if year < 1888:  # the earliest year of a motion picture
            raise ValueError(
                "Invalid year. Year should be greater than or equal to 1888.")
        self.year = year

    def set_genre(self, genre):
        """
        Method to set the genre of the movie.
        """
        self.genre = genre

    def set_release_date(self, release_date):
        """
        Method to set the release date of the movie.
        """
        if not isinstance(release_date, datetime.date):
            raise TypeError(
                "Invalid input. Release date should be of type datetime.date.")
        self.release_date = release_date

    def get_title(self):
        """
        Method to get the title of the movie.
        """
        return self.title

    def get_year(self):
        """
        Method to get the release year of the movie.
        """
        return self.year

    def get_genre(self):
        """
        Method to get the genre of the movie.
        """
        return self.genre

    def get_release_date(self):
        """
        Method to get the release date of the movie.
        """
        return self.release_date
