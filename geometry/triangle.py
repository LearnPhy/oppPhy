from geometry.geometry import Geometry


class Triangle(Geometry):

    def __init__(self, height, floor, subject):
        self.h = height
        self.f = floor
        self.s = subject

    def info(self):
        return f'calculating triangle {self.s} with height = {self.h} and floor = {self.f}'

    def calculate_area(self):
        return self.h * self.f / 2
