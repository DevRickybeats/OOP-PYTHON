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
