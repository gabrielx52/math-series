"""Tests for series.py module."""

import pytest


def test_fib_0():
    """Testing that the zero index of fib is zero."""
    from series import fibonacci
    assert fibonacci(0) == 0


def test_fib_1():
    """Testing that the first index of fib is one"""
    from series import fibonacci
    assert fibonacci(1) == 1


def test_fib_2():
    """Testing that the second index of fib is two"""
    from series import fibonacci
    assert fibonacci(2) == 1
