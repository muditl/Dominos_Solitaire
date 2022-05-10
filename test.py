import pytest

from project.algorithm import *
import numpy as np
from numpy import testing


@pytest.mark.parametrize("n, min_n, max_n",
                         [(1, 10, 20), (2, -10, 0), (3, -15, -5), (20, 2, 5)])
def test_generate_random_grid(n, min_n, max_n):
    res = generate_random_grid(n, min_n, max_n)
    np.testing.assert_equal(n, len(res[0]))
    np.testing.assert_equal(n, len(res[1]))
    assert (not np.any((res < min_n) | (res > max_n)))

    # if sufficiently large array, boundary values should exist
    if n > np.abs(max_n - min_n) / 2:
        assert (np.any(res[0] == max_n) or np.any(res[0] == max_n)) and (
                np.any(res[0] == min_n) or np.any(res[1] == min_n))


@pytest.mark.parametrize("n, min_n, max_n",
                         [(-5, 0, 10), (0, 5, 10), (10, 0, -5), (10, 10, 10)])
def test_boundary_gen_rand_grid(n, min_n, max_n):
    with np.testing.assert_raises(Exception):
        generate_random_grid(n, min_n, max_n)


@pytest.mark.parametrize("grid, length",
                         [([[-1, -2, 3], [1, 5, 6]], 4),
                          ([[10, -20, 23, 4], [0, -1, 2, 5]], 5),
                          ([[10, 0, 223, 4], [0, 1311, 2, 5]], 6),
                          ([[10, -20, 23, 13454], [0, -1, 2, 5]], 7),
                          ([[10, -20, 23, 4], [0, -1, 2, -11145]], 8)])
def test_get_box_len(grid, length):
    np.testing.assert_equal(get_box_len(grid), length)


@pytest.mark.parametrize("i, box_len, expected",
                         [(10, 5, "  10 "), (-24, 7, "  -24  "), (7, 6, "   7  "), (-7, 6, "  -7  ")])
def test_get_str_box(i, box_len, expected):
    actual = get_str_box(i, box_len)
    np.testing.assert_equal(actual, expected)


@pytest.mark.parametrize("grid, expected",
                         [([[-1, -2, 3], [1, 5, 6]], "| -1 | -2 |  3 |\n|  1 |  5 |  6 |"),
                          ([[10, -20, 23, 4], [0, -1, 2, 5]], "|  10 | -20 |  23 |  4  |\n|  0  |  -1 |  2  |  5  |"),
                          ([[10, 0, 223, 4], [0, 1311, 2, 5]],
                           "|  10  |   0  |  223 |   4  |\n|   0  | 1311 |   2  |   5  |"),
                          ([[10, -20, 23, 13454], [0, -1, 2, 5]],
                           "|   10  |  -20  |   23  | 13454 |\n|   0   |   -1  |   2   |   5   |"),
                          ([[10, -20, 23, 4], [0, -1, 2, -11145]],
                           "|   10   |   -20  |   23   |    4   |\n|    0   |   -1   |    2   | -11145 |")])
def test_get_grid_string(grid, expected):
    g_string = get_grid_string(grid)
    np.testing.assert_equal(g_string, expected)


@pytest.mark.parametrize("grid, expected_best, expected_sol",
                         [([[-1], [1]], [2], [False]),
                          ([[10, -20], [0, -15]], [10, 45], [True, True]),
                          ([[-5, -2], [5, 2]], [10, 14], [False, False]),
                          ([[-7, -3, -6, 10], [-5, 1, -8, 4]], [2, 10, 14, 38], [True, True, True, True]),
                          ([[2, 7, 10, -1, 2], [3, 1, 10, 9, 4]], [1, 7, 13, 23, 25],
                           [False, True, True, False, False]),
                          ([[1, -6, 8, 8, 0, -10, 1, -5, -10, -1, -2, -7], [5, 1, 4, 10, 9, -1, 8, 10, -4, -8, -2, -9]],
                           [4, 11, 21, 23, 32, 43, 52, 67, 73, 80, 80, 92],
                           [False, True, True, False, False, True, True, False, False, False, True, True])])
def test_algorithm(grid, expected_best, expected_sol):
    best, solution = dynamic_programming_algorithm(grid)
    np.testing.assert_array_equal(best, expected_best)
    np.testing.assert_array_equal(solution, expected_sol)


@pytest.mark.parametrize("arr, expected",
                         [([0, 0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 1, 1]),
                          ([0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0]),
                          ([1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1]),
                          ([1, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1, 1])])
def test_remove_odd_true(arr, expected):
    remove_odd_true(arr)
    np.testing.assert_array_equal(remove_odd_true(arr), expected)
