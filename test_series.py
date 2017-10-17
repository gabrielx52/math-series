"""Tests for series.py module."""

import pytest

FIB_TEST_DATA = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
                 (7, 13), (8, 21), (9, 34), (10, 55),
                 (11, 89), (23, 28657), (55, 139583862445)]

LUCAS_TEST_DATA = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11),
                   (6, 18), (7, 29), (8, 47), (9, 76), (10, 123),
                   (150, 22291846172619859445381409012498)]


@pytest.mark.parametrize("n, result", FIB_TEST_DATA)
def test_fib(n, result):
    """Testing the fibonnaci function from series module."""
    from series import fibonacci
    assert fibonacci(n) == result


def test_fib_negative():
    """Testing the fibonnaci function from series module for negative input."""
    from series import fibonacci
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.parametrize("n, result", LUCAS_TEST_DATA)
def test_lucas(n, result):
    """Testing the lucas function from series module."""
    from series import lucas
    assert lucas(n) == result


def test_lucas_negative():
    """Test the lucas function from series module for negative input."""
    from series import lucas
    with pytest.raises(ValueError):
        lucas(-1)
