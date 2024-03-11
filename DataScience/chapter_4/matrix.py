from typing import Callable

Matrix = list[list[int]]

Vector = list[int]


def shape(A: Matrix) -> tuple[int, int]:
    # matrix is name with uppercase beacause in math is like it
    num_rows: int = len(A)
    num_cols: int = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    return [a_i[j] for a_i in A]


def make_matrix(
    num_rows: int, num_col: int, entry_fn: Callable[[int, int], int]
) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_col)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


def test_shape() -> None:
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def test_get_row() -> None:
    assert get_row([[1, 2, 3], [4, 5, 6]], 1) == [4, 5, 6]


def test_get_column() -> None:
    assert get_column([[1, 2, 3], [4, 5, 6]], 2) == [3, 6]


def test_identity_matrix() -> None:
    assert identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
