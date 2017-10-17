"""Functions that produce mathmatical series."""


def fibonacci(n):
    """Create fib sequence up to nth."""
    fib_sequence = [0, 1]
    for i in range(n - 1):
        fib_sequence.append(fib_sequence[i + 0] + fib_sequence[i + 1])
    return fib_sequence[n]
