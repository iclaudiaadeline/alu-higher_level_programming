#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that uses BaseGeometry for attribute validation."""


    def __init__(self, width, height):
    """Initializes a Rectangle with width and height, validates them."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
