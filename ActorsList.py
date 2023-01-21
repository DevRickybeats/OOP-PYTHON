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
