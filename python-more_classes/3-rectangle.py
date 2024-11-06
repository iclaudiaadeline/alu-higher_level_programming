#!/usr/bin/python3
"""
an empty Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializes the Rectangle class
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets the width of the Rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        returns the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets the height of the Rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        returns the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns the string representation of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def print(self):
        """
        prints the string representation of the Rectangle
        """
        print(str(self))
