from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


class Triangle(Shape):
    def __init__(self, width: int) -> None:
        self.width = width

    def draw(self) -> None:
        for i in range(self.width):
            print('*' * (i + 1))


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def draw(self) -> None:
        for i in range(self.height):
            print('*' * self.width)


shapes = [Triangle(7), Rectangle(4, 5)]
for shape in shapes:
    shape.draw()
