import random


class MovieRecord:
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
        self.id = random.randint(1000000000, 9999999999)

        # Assign attributes to instance variables
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date

    # Method for Setting Title
    def set_title(self, title):
        """Set the title of the movie.
    Raises: ValueError: If the title is not a string."""
    # Check if the title is a string
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        # Set the title of the movie
        self.title = title

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
        self.genre = genre

    # Method for Setting Release Date
    def set_release_date(self, value):
        # sets the movie release_date
        # throws an exeption if the value is not empty or not of a string type and if the date format is not of the pattern MM/DD/YYYY
        if not isinstance(value, str):
            raise TypeError("Release_date must be a string")
        if not value:
            raise TypeError("Release_date cannot be empty")
        valid: bool = re.search(
            "^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/[0-9]{4}$", value)
        if (not valid):
            raise TypeError(
                "Invalid release_date format, the date should be in MM/DD/YYYY format")
        self.__release_date = value

    # Retrieve Title
    def get_title(self):
        """Retrieve the title of the movie"""
        try:
            return self.title
        except AttributeError:
            print("This movie does not have a title")
            return None

    # Retrieve Year
    def get_year(self):
        """Retrieve the year of release for the movie"""
        try:
            return self.year
        except AttributeError:
            print("This movie does not have a year")
            return None

    # Retrieve Genre
    def get_genre(self):
        """Retrieve the genre of the movie"""
        try:
            return self.genre
        except AttributeError:
            print("This movie does not have a genre")
            return None

    # Retrieve Release Date
    def get_release_date(self):
        """Retrieve the release date of the movie"""
        try:
            return self.release_date
        except AttributeError:
            print("This movie does not have a release date")
            return None


class MovieList:
    """A class to store a collection of movie objects"""

    def __init__(self) -> None:
        """Constructor to create an object of the MovieList class"""
        self.__movieList = []

    def add_movie(self, value):
        """A method to add a movie object to the collection"""
        if not isinstance(value, MovieRecord):  # Check if the argument is a Movie object
            raise TypeError("The argument must be a MoveRecord object")

        self.__movieList.append({
            "id": value.id,
            "genre": value.genre,
            "release_date": value.release_date,
            "title": value.title,
            "year": value.year
        })

    @property
    def movieInfo(self):
        # retrieves the movie store data
        return self.__movieList

    @property
    def movie_length(self):
        # retrieves the total no of movies stored in the collection
        return len(self.__movieList)

    def search_movie_list(self, val, is_genre=False, is_title=False, is_release_date=False):
        """
        Search through the stored movie collection using the genre, release_date or title, 
            - if the user doesn't include a movie attribute in the function params to search by, it defaults to search by title
            - first format the input to all lowercase and the value searching for in order to annul the case-sensitive nature when searching
        """
        if not isinstance(val, str):
            raise TypeError("Search value must be a string")
        if not val:
            raise TypeError("Search value cannot be empty")
        val = val.lower()
        if (not is_genre and not is_title and not is_release_date):
            is_title = True
        for movie in self.__movieList:
            if is_title:
                if movie['title'].lower() == val:
                    return movie
            if is_genre:
                if movie['genre'].lower() == val:
                    return movie
            if is_release_date:
                if movie['release_date'].lower() == val:
                    return movie
        raise Exception("Movie Data not found")

    def remove_movie(self, value):
        """
        Removes the movie that has the title provided in function params value
        first format the input to all lowercase and the value searching for in order to anull the case-sensitive nature when searching
        """
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not value:
            raise TypeError("Title cannot be empty")
        value = value.lower()
        for i in range(len(self.__movieList)):
            if self.__movieList[i]['title'].lower() == value:
                del self.__movieList[i]
                return "Movie Data was Deleted Successfully"
        raise Exception("Movie Data not found")


a1 = MovieRecord('2Sugar', 2022, 'Afro', "1996")
b1 = MovieRecord('PostgreSql', 2015, 'White', '1888')

# print(a1.title)
# print(a1.get_release_date())
# print(a1.get_title())
# a1.set_title('yeah yeah')
# print(a1.get_title())

# m2 = MovieList()
# # print(m2)
# m2.add_movie(a1)
# m2.add_movie(b1)

# print(m2.search_movie_list('PostgreSql'))

movie = MovieRecord(title="Prison Break", year=2000,
                    genre="Hiphop", release_date="13/02/1991")
movie2 = MovieRecord(title="Prison Break", year=2000,
                     genre="", release_date="08/02/1997")
movie3 = MovieRecord(title="Blacklist", year=2018,
                     genre="Comedy", release_date="12/02/2019")
print(movie.id)
print(movie.title)
print(movie.year)
movie.year = 2003
movie.title = "Anti"
print(movie.title)
print(movie.year)
movie.release_date = "12/02/2001"
print(movie.release_date)
print(movie.genre)
print(movie.id)
print(movie.title)
print(movie.year)
movie.year = 2022
movie.genre = "Violence"
movie.title = "Ascramony"
movie.release_date = "09/23/2023"
print(movie.release_date)
print(movie.genre)
print(movie.id)
print(movie.title)
print(movie.year)

movieData = MovieList()
movieData.add_movie(movie)
movieData.add_movie(movie2)
movieData.add_movie(movie3)
print(movieData.movieInfo)
print(movieData.movie_length)
print(movieData.search_movie_list(val="Blacklist"))
print(movieData.remove_movie(value="Prison Break"))
print(movieData.movie_length)
# print(movieData.remove_movie("Prison Break"))
