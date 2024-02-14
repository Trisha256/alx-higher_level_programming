#!/usr/bin/python3
"""Defines a Rectangle."""


class Rectangle:
    """
    Represent a rectangle.

    Attributes:
        width(int): The with of the rectangle.
        height(int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle.

        Args: value(int): The width value to be set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the rectangle.

        Args: value(int): The height value to be set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of a rectangle.

        Returns:
            int: The area of a rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of a rectangle.

        Returns:
            int: The perimeter of a rectangle.
        """
        return (2 * (self_width + self_height))

    def __str__(self):
        """
        Return a string representation of a rectangle.

        Returns:
            str: Representation of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rectangle = (symbol * self.__width + "\n") * self.__height
        return rectangle[:-1]

    def __repr__(self):
        """
        Return a string representation of a rectangle.

        Returns:
            str: Representation of a rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the instance of a Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
