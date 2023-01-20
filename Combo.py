import random

'''Import regex is a module that provides regular expression matching operations.'''
import re


class Movies:
    """A class to represent a movie record"""

    def __init__(self, title, year, genre, release_date):
        """Constructor for MoveRecord class

        Args:
            title (str): The title of the movie.
            year (int): The year the movie was released.
            genre (str): The genre of the movie.
            release_date (str): The date the movie was released.

        Raises: ValueError: If any of the arguments are invalid. """

        '''Check that all arguments are valid'''
        if not isinstance(title, str) or not isinstance(year, int) or not isinstance(genre, str) or not isinstance(release_date, str):
            raise ValueError('Invalid argument type')

        '''Generate a random ID for the move record'''
        self.id = random.randint(1000000000, 9999999999)

        '''Assign attributes to instance variables'''
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date

    '''Method for Setting Title'''

    def set_title(self, title):
        """Set the title of the movie.
    Raises: ValueError: If the title is not a string."""
    # Check if the title is a string
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        # Set the title of the movie
        self.title = title

    '''Method for Setting Year'''

    def set_year(self, year):
        """Set the year of release for the movie.
        Raises: ValueError: If the year is not an integer. """

        '''Check if the year is an integer'''
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        # Set the year of release for the movie
        self._year = year

    '''Method for Setting Genre'''

    def set_genre(self, genre):
        """Set the genre of the movie.
        Raises: ValueError: If genre is not a string. """

        '''Check if genre is a string'''
        if not isinstance(genre, str):
            raise ValueError("Genre must be a string")
        # Set genre of movie
        self.genre = genre

    '''Method for Setting Release Date'''

    def set_release_date(self, value):
        # sets the movie release_date
        # Throws an exception if the value is not null, is not of the string type, or does not have the MM/DD/YYYY date format.
        if not isinstance(value, str):
            raise TypeError("Release_date must be a string")
        if not value:
            raise TypeError("Release_date cannot be empty")
        # This regular expression is used to validate a date in the format MM/DD/YYYY.
        # It checks that the month is between 01 and 12, the day is between 01 and 31,
        # and that there are exactly 4 digits for the year.
        valid: bool = re.search(
            "^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/[0-9]{4}$", value)
        if (not valid):
            raise TypeError(
                "Invalid release_date format, the date should be in MM/DD/YYYY format")
        self.release_date = value

    '''Retrieve Title'''

    def get_title(self):
        """Retrieve the title of the movie"""
        try:
            return self.title
        except AttributeError:
            print("This movie does not have a title")
            return None

    '''Retrieve Year'''

    def get_year(self):
        """Retrieve the year of release for the movie"""
        try:
            return self.year
        except AttributeError:
            print("This movie does not have a year")
            return None

    '''Retrieve Genre'''

    def get_genre(self):
        """Retrieve the genre of the movie"""
        try:
            return self.genre
        except AttributeError:
            print("This movie does not have a genre")
            return None

    '''Retrieve Release Date'''

    def get_release_date(self):
        """Retrieve the release date of the movie"""
        try:
            return self.release_date
        except AttributeError:
            print("This movie does not have a release date")
            return None


class MovieList:
    """A class to store a collection of movie objects"""

    def __init__(self):
        # Constructor to create an object of the MovieList class
        self.__movieList = []

    def add_movie(self, value):
        # A method to add a movie object to the collection
        if not isinstance(value, Movies):  # Check if the argument is a Movie object
            raise TypeError("The argument must be a MoveRecord object")

        self.__movieList.append({
            "id": value.id,
            "genre": value.genre,
            "release_date": value.release_date,
            "title": value.title,
            "year": value.year
        })

    '''retrieves the movie store data'''

    def movieInfo(self):
        return self.__movieList

    '''retrieves the total no of movies stored in the collection'''

    def movie_length(self):
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
        first format the input to all lowercase and the value searching for in order to
        anull the case-sensitive nature when searching
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


class Actors:
    """A class to represent Actors"""
    # A constructor that creates a new movie record with the given details

    def __init__(self, first_name: str, surname: str, gender: str, date_of_birth: str):
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth

    def first_name(self):
        # retrieves the actors first name
        return self.first_name

    def first_name(self, value):
        # sets the first name of the actor
        # throws an exeption if the value is empty or not of a string type
        if not isinstance(value, str):
            raise TypeError("Firstname must be a string")
        if not value:
            raise TypeError("Firstname cannot be empty")
        self.first_name = value

    def surname(self):
        # retrieves the surname of the actor
        return self.surname

    def surname(self, value):
        # sets the surname of the actor
        # throws an exeption if the value is empty or not of a string type
        if not isinstance(value, str):
            raise TypeError("Surname must be a string")
        if not value:
            raise TypeError("Surname cannot be empty")

    def gender(self):
        # retrieves the movie genre
        return self.gender

    # @gender.setter
    def gender(self, value):
        # sets the gender of the actor
        # throws an exeption if the value is not empty or not of a string type
        if not isinstance(value, str):
            raise TypeError("Gender must be a string")
        if not value:
            raise TypeError("Gender cannot be empty")
        self.gender = value

    def date_of_birth(self):
        # retrieves the actors date of birth
        return self.date_of_birth

    def date_of_birth(self, value):
        # sets the movie release_date
        # throws an exeption if the value is not empty or not of a string type and if the date format is not of the pattern MM/DD/YYYY
        if not isinstance(value, str):
            raise TypeError("Date of birth must be a string")
        if not value:
            raise TypeError("Date of birth cannot be empty")
        valid: bool = re.search(
            "^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/[0-9]{4}$", value)
        if (not valid):
            raise TypeError(
                "Invalid release_date format, the date should be in MM/DD/YYYY format")
        self.date_of_birth = value


class Actorslist:
    def __init__(self):
        self.Actorslist = []

    def store_actors_object(self, value):
        if not isinstance(value, Actors):
            raise TypeError("Actor must be of Actors object")
        self.Actorslist.append({
            "first_name": value.first_name,
            "surname": value.surname,
            "gender": value.gender,
            "date_of_birth": value.date_of_birth,
        })

    def remove_actor(self, value):
        """Removes the actor whose firstname is contained in the function parameter value 
        before formatting the input to lowercase and the value being searched for to eliminate 
        the case-sensitivity of the search.
        """

        if not isinstance(value, str):
            raise TypeError("Firstname must be a string")
        if not value:
            raise TypeError("Firstname cannot be empty")
        value = value.lower()
        for i in range(len(self.Actorslist)):
            if self.Actorslist[i]['first_name'].lower() == value:
                del self.Actorslist[i]
                return "Actors Data was Deleted Successfully"
        raise Exception("Actors Data not found")

    def actorsInfo(self):
        # retrieves the actors store data
        return self.Actorslist

    def actors_length(self):
        # retrieves the total no of actors stored in the collection
        return len(self.Actorslist)

    def search_actors_list(self, val, is_first_name=True):
        """
        Search through the stored actors collection using the firstname,
        - first format the input to all lowercase and the value searching for in order to annul the case-sensitive nature when searching
        """
        if not isinstance(val, str):
            raise TypeError("Search value must be a string")
        if not val:
            raise TypeError("Search value cannot be empty")
        val = val.lower()

        for actor in self.Actorslist:
            if actor['first_name'].lower() == val:
                return actor
        raise Exception("Actor Data not found")


'''A movie object named ‘007’ with all the details required for a movie'''
themovie007 = Movies(title="James Bond", year=2022,
                     genre="Action", release_date="11/11/2022")

'''A movie list object named ‘actions’ that contains the ‘007’ object in the object’s collection.'''
actions = MovieList()
actions.add_movie(themovie007)

'''An actor object named ‘JamesBond’ with all the details required for an actor in the class'''
JamesBond = Actors('James', 'Bond', 'Male', '13/11/1980')

'''An actor list object named ‘all_actors’ that contains ‘JamesBond’ object in the object’s collection.'''
all_actors = Actorslist()
all_actors.store_actors_object(JamesBond)

'''A statement to call the movie object method to get all the detail of the movie object “007”.'''
print(themovie007.get_title())
print(themovie007.get_year())
print(themovie007.get_genre())
print(themovie007.get_release_date())

'''A statement to call the actor list object method to get the number of objects in its collection.'''
print(all_actors.actors_length())

'''A statement to call the actor list object method to get the details of the actor James Bond'''
print(all_actors.actorsInfo())

'''A statement to call the actor list object method to remove the details of the actor 
James Bond from the collection'''
print(all_actors.remove_actor("James"))

'''A statement to call the actor list object method to get the number of objects in its collection.'''
print(all_actors.actors_length())
