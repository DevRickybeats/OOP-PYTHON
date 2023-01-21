import datetime


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
