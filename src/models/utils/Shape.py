class Shape:
    """
    A class representing a 3D shape with length, width, and height.

    Attributes:
        length (float): The length of the shape.
        width (float): The width of the shape.
        height (float): The height of the shape.
        volume (float): The calculated volume of the shape.

    Methods:
        volume: Calculates and returns the volume of the shape.
        _validate_dimensions: Validates that all dimensions are
                              positive numbers.
    """

    def __init__(self, length: float, width: float, height: float) -> None:
        """
        Initializes the Shape with length, width, and height.

        Args:
            length (float): The length of the shape.
            width (float): The width of the shape.
            height (float): The height of the shape.

        Raises:
            ValueError: If any of the dimensions are not positive numbers.
        """
        self._validate_dimensions(length, width, height)
        self.length = length
        self.width = width
        self.height = height

    @staticmethod
    def _validate_dimensions(
        length: float, width: float, height: float
    ) -> None:
        """
        Validates that the given dimensions are positive numbers.

        Args:
            length (float): The length of the shape.
            width (float): The width of the shape.
            height (float): The height of the shape.

        Raises:
            ValueError: If any of the dimensions are not positive numbers.
        """
        if not all(
            isinstance(x, (int, float)) and x > 0
            for x in (length, width, height)
        ):
            raise ValueError("Dimensions must be positive numbers")

    @property
    def volume(self) -> float:
        """
        Calculates the volume of the shape.

        Returns:
            float: The volume of the shape, calculated as:
                length * width * height.
        """
        return self.length * self.width * self.height
