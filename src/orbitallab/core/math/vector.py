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
