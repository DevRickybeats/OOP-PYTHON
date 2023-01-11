import re


class Actors:
    """A class to represent Actors"""

    def __init__(self, first_name: str, surname: str, gender: str, date_of_birth: str) -> None:
        """<< A constructor that creates a new movie record with the given details >>"""
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
    #

    @property
    def first_name(self):
        # retrieves the actors first name
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        # sets the first name of the actor
        # throws an exeption if the value is empty or not of a string type
        if not isinstance(value, str):
            raise TypeError("Firstname must be a string")
        if not value:
            raise TypeError("Firstname cannot be empty")
        self.first_name = value

    @property
    def surname(self):
        # retrieves the surname of the actor
        return self.surname

    @surname.setter
    def surname(self, value):
        # sets the surname of the actor
        # throws an exeption if the value is empty or not of a string type
        if not isinstance(value, str):
            raise TypeError("Surname must be a string")
        if not value:
            raise TypeError("Surname cannot be empty")

    @property
    def gender(self):
        # retrieves the movie genre
        return self.gender

    @gender.setter
    def gender(self, value):
        # sets the gender of the actor
        # throws an exeption if the value is not empty or not of a string type
        if not isinstance(value, str):
            raise TypeError("Gender must be a string")
        if not value:
            raise TypeError("Gender cannot be empty")
        self.gender = value

    @property
    def date_of_birth(self):
        # retrieves the actors date of birth
        return self.date_of_birth

    @date_of_birth.setter
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
    def __init__(self) -> None:
        self.Actorslist = []

    def store_actors_objet(self, value):
        if not isinstance(value, Actors):
            raise TypeError("Actor must be of Actors object")
        self.Actorslist.append({
            "first_name": value.first_name,
            "surname": value.surname,
            "gender": value.gender,
            "date_of_birth": value.date_of_birth,
        })

    def remove_actor(self, value):
        """
        Removes the actor that has the firstname provided in function params value
        first format the input to all lowercase and the value searching for in order
        to anull the case-sensitive nature when searching
        """
        if not isinstance(value, str):
            raise TypeError("Firstname must be a string")
        if not value:
            raise TypeError("Firstname cannot be empty")
        value = value.lower()
        for i in range(len(self.Actorslist)):
            if self.Actorslist[i]['title'].lower() == value:
                del self.Actorslist[i]
                return "Actors Data was Deleted Successfully"
        raise Exception("Actors Data not found")

    @property
    def actorsInfo(self):
        # retrieves the actors store data
        return self.Actorslist

    @property
    def actors_length(self):
        # retrieves the total no of actors stored in the collection
        return len(self.Actorslist)
