"""Tests for series.py module."""

import pytest

TEST_DATA = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
             (7, 13), (8, 21), (9, 34), (10, 55),
             (11, 89), (23, 28657), (55, 139583862445)]


@pytest.mark.parametrize("n, result", TEST_DATA)
def test_fib(n, result):
    """Testing the fibonnaci function from series module."""
    from series import fibonacci
    assert fibonacci(n) == result


def test_fib_none():
    """."""
    from series import fibonacci
    with pytest.raises(ValueError):
        fibonacci(-1)
