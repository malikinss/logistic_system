from .utils import AutoIDMixin
from .utils import Shape


class Package(Shape, AutoIDMixin):
    """
    Represents a package with dimensions and a unique ID.

    This class combines the functionality of the Shape and AutoIDMixin
    classes. It provides a way to create packages with specific dimensions
    (length, width, height) while automatically assigning each package
    a unique ID.

    Attributes:
        id (int): A unique identifier for the package, automatically
            assigned by AutoIDMixin.
        length (float): The length of the package.
        width (float): The width of the package.
        height (float): The height of the package.
        volume (float): The volume of the package, calculated using the
            provided dimensions.

    Methods:
        __init__: Initializes the package with its dimensions and a unique
            ID, and calculates its volume.
    """

    def __init__(self, length, width, height):
        """
        Initializes a new package with the specified dimensions.

        This method calls the initializers for both the Shape (to set up
        dimensions and volume) and AutoIDMixin (to assign a unique ID).

        Args:
            length (float): The length of the package.
            width (float): The width of the package.
            height (float): The height of the package.

        Calls:
            AutoIDMixin.__init__: Initializes the unique ID for the package.
            Shape.__init__: Initializes the dimensions and calculates the
            volume of the package.
        """
        # Initialize AutoIDMixin to assign the unique ID
        AutoIDMixin.__init__(self)

        # Initialize Shape with length, width, and height
        Shape.__init__(self, length, width, height)
