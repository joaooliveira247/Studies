Vector = list[int]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: list[Vector]) -> Vector:
    assert vectors, "no vectors provided"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "diferents sizes!"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(c: int, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


def vector_mean(vectors: list[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot_product(v: Vector, w: Vector) -> int:
    assert len(v) == len(w), "vectors must  be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> int:
    return dot_product(v, v)


def magnitude(v: Vector) -> int:
    return sum_of_squares(v) ** (1 / 2)


def square_distance(v: Vector, w: Vector) -> int:
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> int:
    return magnitude(subtract(v, w))


def test_add() -> None:
    assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def test_subtract() -> None:
    assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def test_vector_sum() -> None:
    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def test_scalar_multiply() -> None:
    assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def test_vector_mean() -> None:
    assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def test_dot_product() -> None:
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def test_sum_of_squares() -> None:
    assert sum_of_squares([1, 2, 3]) == 14


def test_magnitude() -> None:
    assert magnitude([3, 4]) == 5
