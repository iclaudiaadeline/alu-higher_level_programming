#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
The Rectangle class validates and initializes width and height using 
BaseGeometry's integer_validator.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle using BaseGeometry for validation.
    
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance after validating width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
