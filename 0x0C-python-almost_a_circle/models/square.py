#!/usr/bin/python3
""" Square Moddel """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ string of square class """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """ Assign attribute """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ To dictionary """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
