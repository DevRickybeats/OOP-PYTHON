import random


class MoveRecord:
    """A class to represent a movie record"""

    def __init__(self, title, year, genre, release_date):
        """Constructor for MoveRecord class

        Args:
            title (str): The title of the movie.
            year (int): The year the movie was released.
            genre (str): The genre of the movie.
            release_date (str): The date the movie was released.

        Raises: ValueError: If any of the arguments are invalid. """

        # Check that all arguments are valid
        if not isinstance(title, str) or not isinstance(year, int) or not isinstance(genre, str) or not isinstance(release_date, str):
            raise ValueError('Invalid argument type')

        # Generate a random ID for the move record
        self._id = random.randint(1000000000, 9999999999)

        # Assign attributes to instance variables
        self._title = title
        self._year = year
        self._genre = genre
        self._release_date = release_date

    # Method for Setting Title
    def set_title(self, title):
        """Set the title of the movie.
    Raises: ValueError: If the title is not a string."""
    # Check if the title is a string
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        # Set the title of the movie
        self._title = title

    # Method for Setting Year
    def set_year(self, year):
        """Set the year of release for the movie.
        Raises: ValueError: If the year is not an integer. """

    # Check if the year is an integer
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        # Set the year of release for the movie
        self._year = year

    # Method for Setting Genre
    def set_genre(self, genre):
        """Set the genre of the movie.
        Raises: ValueError: If genre is not a string. """

    # Check if genre is a string
        if not isinstance(genre, str):
            raise ValueError("Genre must be a string")
        # Set genre of movie
        self._genre = genre

    # Method for Setting Release Date
    def set_release_date(self, release_date):
        """Set release date of movie.
        Args:release_date (datetime object): Release date of movie.
        Raises: TypeError: If release date is not a datetime object."""

    # Check if release date is datetime object
        if not isinstance(release_date, datetime.datetime):
            raise TypeError("Release date must be a datetime object")
        # Set release date of movie
        self._release_date = release_date

    # Retrieve Title
    def get_title(self):
        """Retrieve the title of the movie"""
        try:
            return self._title
        except AttributeError:
            print("This movie does not have a title")
            return None

    # Retrieve Year
    def get_year(self):
        """Retrieve the year of release for the movie"""
        try:
            return self._year
        except AttributeError:
            print("This movie does not have a year")
            return None

    # Retrieve Genre
    def get_genre(self):
        """Retrieve the genre of the movie"""
        try:
            return self._genre
        except AttributeError:
            print("This movie does not have a genre")
            return None

    # Retrieve Release Date
    def get_release_date(self):
        """Retrieve the release date of the movie"""
        try:
            return self._release_date
        except AttributeError:
            print("This movie does not have a release date")
            return None


class MovieList:
    """A class to store a collection of movie objects"""

    def __init__(self):
        """Constructor to create an object of the MovieList class"""
        self.movies = {}  # Dictionary to store movie objects

    def add_movie(self, movie):
        """A method to add a movie object to the collection"""
        if not isinstance(movie, MoveRecord):  # Check if the argument is a Movie object
            raise TypeError("The argument must be a MoveRecord object")

        # Add the movie object to the dictionary with its title as key and itself as value
        self.movies[movie._title] = movie

    def search_movie(title, genre, release_date):
        """Searches through the movie collection and finds a movie by one or more of the following movie attributes: title, genre or release date.
        Parameters:
        title (str): The title of the movie to search for.
        genre (str): The genre of the movie to search for.
        release_date (int): The release date of the movie to search for.
        Returns:A list of movies that match the given criteria. """

        # Initialize an empty list to store matching movies
        matching_movies = []

        # Iterate through each movie in the collection
        for movie in MoveRecord:
            # Check if all criteria match
            if (title == movie.title or title == None) and (genre == movie.genre or genre == None) and (release_date == movie.release_date or release_date == None):

                # If all criteria match, add it to the list of matching movies
                matching_movies.append(movie)

            # Return the list of matching movies
            return matching_movies

    def remove_movie(title):
        """Removes a movie from the collection based on its title.
        Parameters:
        title (str): The title of the movie to be removed from the collection.
        Returns: True if successful, False otherwise."""

       # Iterate through each movie in the collection
       for i in range(len(movies)):

            # Check if titles match
            if movies[i].title == title:

                # If titles match, remove it from the collection
                del movies[i]

                # Return True as removal was successful
                return True

        # Return False as removal was unsuccessful
        return False


a1 = MoveRecord('2Sugar', 2022, 'Afro', "1996")

print(a1._title)
print(a1.get_release_date())
print(a1.get_title())
a1.set_title('yeah yeah')
print(a1.get_title())
