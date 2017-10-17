"""Tests for series.py module."""

import pytest


def test_fib_0():
    """Testing that the zero index of fib is zero."""
    from series import fibonacci
    assert fibonacci(0) == 0
