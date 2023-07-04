#!/usr/bin/python3
""" This is a rectangle module """


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        number_of_instances (int): Number of instances of Rectangle.
        print_symbol: Symbol used for string representation.

    Args:
        width (int): Width of the rectangle (default is 0).
        height (int): Height of the rectangle (default is 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): Width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): Height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + '\n'
        return (rectangle_str.strip())

    def __repr__(self):
        """
        Returns a strihe rectangle for recreating an instance.

        Returns:
            str: String representation of the rectangle.
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """
        Deletes  and decrements the number_of_instances attribute.

        Prints a farewell message when the instance is deleted.
        """
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return (rect_1)
        if rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
