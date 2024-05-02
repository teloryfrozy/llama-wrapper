"""
Represents a decimal number with integer and fractional parts.
"""

class DecimalNumber:
    """Represents a decimal number with integer and fractional parts."""

    def __init__(self, integer_part: int, fractional_part: int):
        """
        Initialize a DecimalNumber object.

        Args:
            integer_part (int): The integer part of the decimal number.
            fractional_part (int): The fractional part of the decimal number.
        """
        self.integer_part = integer_part
        self.fractional_part = fractional_part
        self.fractional_digits = 2

    def __eq__(self, other):
        """
        Compare two DecimalNumber objects for equality.

        Args:
            other (DecimalNumber): The other DecimalNumber object to compare.

        Returns:
            bool: True if the two objects are equal, False otherwise.

        Raises:
            TypeError: If the other object is not a DecimalNumber.
        """
        if isinstance(other, DecimalNumber):
            return (
                self.integer_part == other.integer_part
                and self.fractional_part == other.fractional_part
            )
        raise TypeError("Equality comparison with non-DecimalNumber object")

    def __repr__(self):
        """
        Return a string representation of the DecimalNumber.

        Returns:
            str: The string representation of the DecimalNumber.
        """
        return f"{self.integer_part}.{self.fractional_part:0{self.fractional_digits}d}"
