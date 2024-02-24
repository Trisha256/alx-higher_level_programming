#!/usr/bin/python3

"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None)
    """Initiates a new rectangle.

    Args:
        width(int): width of the rectangle.
        height(int): height of the rectangle.
        x(int): x coordinate of the rectangle.
        y(int): y coordinate of the rectangle.
        id(int): the identity of the rectangle.
    Raises:
        TypeError: if either of width or height is not int.
        ValueError: if either of width or height <= 0.
        TypeError: if either of x or y is not int.
        ValueError: if eith of x or y is < 0.
    """
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get/set the x cordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get/set the y cordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """return the area of the rectangle."""
        return self.width * self. height
    
    def display(self):
        """prints the rectangle using the "#" character."""
        if self.width == 0 or self.height == 0
        print("")
        return
        
        [print("") for y in range (self.y)]
        for h in range (self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    
    def __str__(self):
        """Returns the print() and str() representation of a circle."""
        return [Rectangle] ({}) {}/{} - {}/{}.format(self.id, self.x,
                                                     self.y, self.width,
                                                     self.height)
        





