#!/usr/bin/python3
"""
module square qui va heriter de class rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square qui herite de rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """
        retourne la représentation en string du carré
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
