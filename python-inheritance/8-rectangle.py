#!/usr/bin/python3
""This modules defines a rectangle class that inherits from  BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class  that represents Rectangle"""

    def __init__(self, width, height):
        """Initialize  a rectangle  instantce after validating width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
