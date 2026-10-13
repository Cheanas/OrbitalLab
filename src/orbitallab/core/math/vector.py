from __future__ import annotations

import math
from dataclasses import dataclass
from types import NotImplementedType


@dataclass(frozen=True, slots=True)
class Vector2D:
    x: float
    y: float

    def __add__(self, other: object) -> Vector2D | NotImplementedType:
        if not isinstance(other, Vector2D):
            return NotImplemented

        x: float = self.x + other.x
        y: float = self.y + other.y

        return Vector2D(x, y)

    def __sub__(self, other: object) -> Vector2D | NotImplementedType:
        if not isinstance(other, Vector2D):
            return NotImplemented

        x: float = self.x - other.x
        y: float = self.y - other.y

        return Vector2D(x, y)

    def __mul__(self, other: object) -> Vector2D | NotImplementedType:
        if isinstance(other, bool):
            return NotImplemented

        if not isinstance(other, int | float):
            return NotImplemented

        x: float = self.x * other
        y: float = self.y * other
        return Vector2D(x, y)

    def __rmul__(self, other: object) -> Vector2D | NotImplementedType:
        return self.__mul__(other)

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def normalize(self) -> Vector2D:
        #Avoid /0
        if self.x == 0 and self.y ==0:
            raise ValueError("cannot normalize a zero vector")
        
        magnitude = self.magnitude()
        normalised_vector = Vector2D(self.x* (1/magnitude), self.y* (1/magnitude))
        
        return normalised_vector