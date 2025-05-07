from .utils import AutoIDMixin
from .utils import Shape


class Truck(Shape, AutoIDMixin):
    """
    Represents a truck that can hold packages with dimensions and a unique ID.

    This class combines the functionality of the Shape and AutoIDMixin
    classes. It represents a truck that has specific dimensions and
    can hold multiple packages, each identified by a unique ID.

    Attributes:
        id (int): A unique identifier for the truck, automatically
            assigned by AutoIDMixin.
        length (float): The length of the truck.
        width (float): The width of the truck.
        height (float): The height of the truck.
        volume (float): The volume of the truck, calculated using the
            provided dimensions.
        packages (list): A list of package IDs that are added to the truck.

    Methods:
        __init__: Initializes the truck with its dimensions, a unique ID,
            and an empty list of packages.
        add_package: Adds a package ID to the truck's list of packages.
    """

    def __init__(self, length, width, height):
        """
        Initializes a new truck with the specified dimensions and a unique ID.

        This method calls the initializers for both the Shape (to set up
        dimensions and volume) and AutoIDMixin (to assign a unique ID).
        Additionally, it initializes an empty list to hold package IDs.

        Args:
            length (float): The length of the truck.
            width (float): The width of the truck.
            height (float): The height of the truck.

        Calls:
            AutoIDMixin.__init__: Initializes the unique ID for the truck.
            Shape.__init__: Initializes the dimensions and calculates the
            volume of the truck.
        """
        # Initialize AutoIDMixin to assign the unique ID
        AutoIDMixin.__init__(self)

        # Initialize Shape with length, width, and height
        Shape.__init__(self, length, width, height)

        # Initialize the packages list
        self.packages = []

    def add_package(self, package_id):
        """
        Adds a package ID to the truck's list of packages.

        This method appends the given package ID to the truck's packages list.

        Args:
            package_id (int): The unique ID of the package to be added.
        """
        self.packages.append(package_id)
