import random
import datetime


class Movies:
    def __init__(self, title, year, genre, release_date):
        """
        Constructor method to create new movie records with a randomly generated ID, title, year, genre and release date.
        """
        self.id = random.randint(1, 10000)
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date

    def set_title(self, title):
        """
        Method to set the title of the movie.
        """
        self.title = title

    def set_year(self, year):
        """
        Method to set the release year of the movie.
        """
        if year < 1888:
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


class MovieList:
    def __init__(self):
        """
        Constructor method to create an object of the MovieList class.
        """
        self.movies = {}

    def add_movie(self, movie_obj):
        """
        Method to store a movie object in the collection.
        """
        self.movies[movie_obj.id] = movie_obj

    def search_movie(self, title=None, genre=None, release_date=None):
        """
        Method to search through the collection and find a movie by one or more of the following movie attributes: title, genre or release date.
        """
        result = []
        for movie in self.movies.values():
            if title and movie.get_title() != title:
                continue
            if genre and movie.get_genre() != genre:
                continue
            if release_date and movie.get_release_date() != release_date:
                continue
            result.append(movie)
        return result

    def remove_movie(self, title):
        """
        Method to remove a movie from the collection based on the title of the movie.
        """
        for movie in self.movies.values():
            if movie.get_title() == title:
                del self.movies[movie.id]
                return True
        raise ValueError("Movie not found.")

    def get_movie_count(self):
        """
        Method to calculate and return the total number of movies stored in the collection.
        """
        return len(self.movies)


class Actors:
    def __init__(self, first_name, surname, gender, date_of_birth):
        """
        Constructor method to create new actor records with the following details: first name, surname, gender and date of birth.
        """
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth

    def set_first_name(self, first_name):
        """
        Method to set the first name of the actor.
        """
        self.first_name = first_name

    def set_surname(self, surname):
        """
        Method to set the surname of the actor.
        """
        self.surname = surname

    def set_gender(self, gender):
        """
        Method to set the gender of the actor.
        """
        if not gender:
            raise ValueError("Gender cannot be empty")
        elif gender not in ['male', 'female']:
            raise ValueError(
                "Invalid gender. Gender should be either 'male' or 'female'.")
        self.gender = gender

    def set_date_of_birth(self, date_of_birth):
        """
        Method to set the date of birth of the actor.
        """
        if not isinstance(date_of_birth, datetime.date):
            raise TypeError(
                "Invalid input. Date of birth should be of type datetime.date.")
        self.date_of_birth = date_of_birth

    def get_first_name(self):
        """
        Method to get the first name of the actor.
        """
        return self.first_name

    def get_surname(self):
        """
        Method to get the surname of the actor.
        """
        return self.surname

    def get_gender(self):
        """
        Method to get the gender of the actor.
        """
        return self.gender

    def get_date_of_birth(self):
        """
        Method to get the date of birth of the actor.
        """
        return self.date_of_birth


class ActorsList:
    def __init__(self):
        """
        Constructor method to create an object of the ActorsList class.
        """
        self.actors = {}

    def add_actor(self, actor_obj):
        """
        Method to store an actor object in the collection.
        """
        self.actors[actor_obj.first_name] = actor_obj

    def remove_actor(self, first_name):
        """
        Method to remove an actor from the collection by giving the actor’s first name.
        """
        if first_name not in self.actors:
            raise ValueError("Actor not found.")
        del self.actors[first_name]
        print("\nActor removed from the collection")

    def get_actor_count(self):
        """
        Method to count the number of actors in the system.
        """
        return len(self.actors)

    def get_actor_by_name(self, first_name):
        """
        Method to return the details of an actor based on the first name of the actor.
        """
        if first_name not in self.actors:
            raise ValueError("Actor not found.")
        return self.actors[first_name]


# create a movie object named '007'
movie_007 = Movies("007", 2020, "Action", datetime.datetime(2002, 2, 25))

# create a movie list object named 'actions'
actions = MovieList()
actions.add_movie(movie_007)

# create an actor object named 'JamesBond'
james_bond = Actors("James", "Bond", "Male", datetime.datetime(1960, 1, 1))

# create an actor list object named 'all_actors'
all_actors = ActorsList()
all_actors.add_actor(james_bond)

# call the movie object method to get all the detail of the movie object "007"
print("Details of movie 007:")
print("Title:", movie_007.get_title())
print("Year:", movie_007.get_year())
print("Genre:", movie_007.get_genre())
print("Release date:", movie_007.get_release_date())

# call the actor list object method to get the number of objects in its collection
print("\nNumber of actors in the collection:", all_actors.get_actor_count())

# call the actor list object method to get the details of the actor James Bond
print("\nDetails of actor James Bond:")
print("First Name:", james_bond.get_first_name())
print("Surname:", james_bond.get_surname())
print("Gender:", james_bond.get_gender())
print("Date of birth:", james_bond.get_date_of_birth())

# call the actor list object method to remove the details of the actor James Bond from the collection
all_actors.remove_actor("James")

# call the actor list object method to get the number of objects in its collection
print("\nNumber of actors in the collection:", all_actors.get_actor_count())
