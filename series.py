"""Functions that produce mathmatical series."""


def fibonacci(n):
    """Return the nth item of the fibonacci sequence."""
    fib_sequence = [0, 1]
    if n < 0:
        raise ValueError("Please input positive integers only.")
    for i in range(n - 1):
        fib_sequence.append(fib_sequence[i] + fib_sequence[i + 1])
    return fib_sequence[n]


def lucas(n):
    """Return the nth item of the lucas sequence."""
    lucas_sequence = [2, 1]
    if n < 0:
        raise ValueError("Please input positive integers only.")
    for i in range(n - 1):
        lucas_sequence.append(lucas_sequence[i] + lucas_sequence[i + 1])
    return lucas_sequence[n]


def sum_series(n, zero_indx=0, first_indx=1):
    """Return the nth item of the sum series sequence."""
    sum_sequence = [zero_indx, first_indx]
    if n < 0:
        raise ValueError("Please input positive integers only.")
    for i in range(n - 1):
        sum_sequence.append(sum_sequence[i] + sum_sequence[i + 1])
    return sum_sequence[n]
