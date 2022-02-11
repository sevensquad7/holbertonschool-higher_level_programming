#!/usr/bin/python3
"""define Rectangle"""


from models.base import Base


class Rectangle(Base):
    """define class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define contructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        '''Set width'''
        self.__width = width

    @property
    def height(self):
        '''Get height'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Set height'''
        self.__height = height

    @property
    def x(self):
        '''Get x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''Set x'''
        self.__x = x

    @property
    def y(self):
        '''Get y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''Set y'''
        self.__y = y

def validator_integer(self, name, value, flag):
    """validate integer"""
    if type (value) in not int:
        raise TypeError ("{} must be a integer".format(name))
    if flag == 1:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
    if flag == 2:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
