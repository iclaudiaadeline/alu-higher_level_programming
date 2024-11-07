#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It implements a rectangle with validated width and height attributes.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    
    This class represents a rectangle with width and height dimensions.
    Both dimensions must be positive integers and are validated using
    the integer_validator method inherited from BaseGeometry.
    
    Attributes:
        __width (int): The width of the rectangle (private)
        __height (int): The height of the rectangle (private)
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            
        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
