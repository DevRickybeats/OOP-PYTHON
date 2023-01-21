import Movies
import MovieList
import Actors
import ActorsList
import datetime

# create a movie object named '007'
movie_007 = Movies.Movies()
movie_007.set_title('007')
movie_007.set_year(2020)
movie_007.set_genre('Action')
movie_007.set_release_date(datetime.date(2018, 11, 1))

# create a movie list object named 'actions'
actions = MovieList.MovieList()
actions.add_movie(movie_007)

# create an actor object named 'JamesBond'
james_bond = Actors.Actors("James", "Bond", "Male",
                           datetime.datetime(1960, 1, 1))

# create an actor list object named 'all_actors'
all_actors = ActorsList.ActorsList()
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

print(all_actors.get_actor_by_name('James'))

# call the actor list object method to remove the details of the actor James Bond from the collection
all_actors.remove_actor("James")

# call the actor list object method to get the number of objects in its collection
print("\nNumber of actors in the collection:", all_actors.get_actor_count())
