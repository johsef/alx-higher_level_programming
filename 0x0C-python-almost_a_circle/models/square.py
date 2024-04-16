#!/usr/bin/python3
"""Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set the value of the width of Square"""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns attributes to arguments"""
        if args and kwargs is not None:
            for arg in range(len(args)):
                val = args[arg]
                if arg == 0:
                    self.id = val
                if arg == 1:
                    self.size = val
                if arg == 2:
                    self.x = val
                if arg == 3:
                    self.y = val
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """Returns a printable string of the Square instance"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
