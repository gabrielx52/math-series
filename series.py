"""Functions that produce mathmatical series."""


def fibonacci(n):
    """Return the nth item of the fibonacci sequence."""
    fib_sequence = [0, 1]
    if n < 0:
        raise ValueError("Please input positive integers only.")
    for i in range(n - 1):
        fib_sequence.append(fib_sequence[i + 0] + fib_sequence[i + 1])
    return fib_sequence[n]


def lucas(n):
    """Return the nth item of the lucas sequence."""
    lucas_sequence = [2, 1]
    return lucas_sequence[n]
