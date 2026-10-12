"""Testing vector.py file"""

import pytest

from orbitallab.core.math.vector import Vector2D


def test_vector_add_invalid_type() -> None:
    value1 = Vector2D(12, 25)
    value2 = 2
    with pytest.raises(TypeError):
        value1 + value2  # pyright: ignore[reportUnusedExpression]

    assert value1.__add__(value2) is NotImplemented


def test_vector_add_valid_type() -> None:
    value1 = Vector2D(2, 3)
    value2 = Vector2D(3, 2)
    result1 = value1 + value2
    expected_result = Vector2D(5, 5)
    assert result1 == expected_result
    assert result1 is not value1
    assert value1 == Vector2D(2, 3)
    assert value2 == Vector2D(3, 2)


def test_vector_sub_invalid_type() -> None:
    value1 = Vector2D(12, 25)
    value2 = 2
    with pytest.raises(TypeError):
        value1 - value2  # pyright: ignore[reportUnusedExpression]

    assert value1.__sub__(value2) is NotImplemented


def test_vector_sub_valid_type() -> None:
    value1 = Vector2D(2, 3)
    value2 = Vector2D(3, 2)
    result1 = value1 - value2
    result2 = value1 - value1
    result3 = value2 - value1
    expected_result = Vector2D(-1, 1)
    expected_result2 = Vector2D(0, 0)
    expected_result3 = Vector2D(1, -1)
    assert result1 == expected_result
    assert result1 is not value1
    assert result2 == expected_result2
    assert result3 == expected_result3
    assert value1 == Vector2D(2, 3)
    assert value2 == Vector2D(3, 2)


def test_vector_mul_invalid_type() -> None:
    value1 = Vector2D(2, 3)
    value2 = Vector2D(3, 2)
    value3 = "5"
    value4 = True
    with pytest.raises(TypeError):
        value1 * value2  # pyright: ignore[reportUnusedExpression]

    with pytest.raises(TypeError):
        value1 * value3  # pyright: ignore[reportUnusedExpression]

    with pytest.raises(TypeError):
        value1 * value4  # pyright: ignore[reportUnusedExpression]


def test_vector_mul_valid_type() -> None:
    value1 = Vector2D(2, 3)
    value2 = 1
    value3 = 2
    value4 = -2
    value5 = 0.5
    value6 = -0.5
    value7 = 0
    result2 = Vector2D(2, 3)
    result3 = Vector2D(4, 6)
    result4 = Vector2D(-4, -6)
    result5 = Vector2D(1, 1.5)
    result6 = Vector2D(-1, -1.5)
    result7 = Vector2D(0, 0)

    assert value1 * value2 == result2
    assert value1 * value3 == result3
    assert value1 * value4 == result4
    assert value1 * value5 == result5
    assert value1 * value6 == result6
    assert value1 * value7 == result7


rmull_vectors =[
    (Vector2D(2, 3), 1, Vector2D(2, 3)),
    (Vector2D(2, 3), 2, Vector2D(4, 6)),
    (Vector2D(2, 3),-2, Vector2D(-4, -6)),
    (Vector2D(2, 3), 0.5, Vector2D(1, 1.5)),
    (Vector2D(2, 3), -0.5, Vector2D(-1, -1.5)),
    (Vector2D(2, 3), 0, Vector2D(0, 0)),   
    (Vector2D(2, 3), True, Vector2D(0, 0))   
]
@pytest.mark.parametrize("input, multiplier, expected", rmull_vectors)
def test_vector_rmul(input: Vector2D, multiplier: float, expected: Vector2D) -> None:

    if isinstance(multiplier, bool):
        with pytest.raises(TypeError):
            multiplier * input  # pyright: ignore[reportUnusedExpression]
    else:
        assert multiplier * input == expected

vectors = [
    (Vector2D(3, 4), 5),
    (Vector2D(-3, -4), 5),
    (Vector2D(0, 0), 0),
    (Vector2D(7, 0), 7),
    (Vector2D(0, -9), 9),
]

@pytest.mark.parametrize("vector, expected", vectors)
def test_magnitude(vector: Vector2D, expected: float) -> None:
    assert vector.magnitude() == pytest.approx(expected)
