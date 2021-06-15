from geometry.geometry import Geometry


class Rectangle(Geometry):

    def __init__(self, length, height):
        self.l = length
        self.h = height

    def info(self):
        return 'module contains all of formula on rectangle'

    def calculate_area(self):
        return self.l * self.h
