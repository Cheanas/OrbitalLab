"""Testing add method against wrong typing"""

from __future__ import annotations

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


def test_vector_rmull_valid_type() -> None:
    value1 = Vector2D(2, 3)
    value2 = 1
    value3 = 2
    value4 = -2
    value5 = 0.5
    value6 = -0.5
    value7 = 0
    value8 = True

    result2 = Vector2D(2, 3)
    result3 = Vector2D(4, 6)
    result4 = Vector2D(-4, -6)
    result5 = Vector2D(1, 1.5)
    result6 = Vector2D(-1, -1.5)
    result7 = Vector2D(0, 0)

    assert value2 * value1 == result2
    assert value3 * value1 == result3
    assert value4 * value1 == result4
    assert value5 * value1 == result5
    assert value6 * value1 == result6
    assert value7 * value1 == result7

    with pytest.raises(TypeError):
        value8 * value1  # pyright: ignore[reportUnusedExpression]
