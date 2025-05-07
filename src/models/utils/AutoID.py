class AutoIDMixin:
    """
    Mixin class that auto-generates unique IDs for each instance.

    This mixin ensures that each instance of a class that includes it
    automatically gets a unique ID. The ID starts at 1 and increments
    for each new instance of the class.

    Attributes:
        id (int): A unique identifier for each instance of the class.

    Methods:
        __init__: Initializes an instance with a unique ID and increments
            the class-level ID counter.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance with a unique ID.

        This method assigns a unique `id` to each instance based on a
        class-level counter. The counter starts at 1 and increments with
        each new instance.

        Args:
            *args: Variable length argument list for initialization.
            **kwargs: Arbitrary keyword arguments for initialization.

        Sets:
            self.id: A unique ID for the instance, starting from 1.
        """
        cls = self.__class__
        # Check if the class has an ID counter, initialize it if not
        if not hasattr(cls, "_id_counter"):
            cls._id_counter = 1
        self.id = cls._id_counter
        cls._id_counter += 1
        super().__init__(*args, **kwargs)
