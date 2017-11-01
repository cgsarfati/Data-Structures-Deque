""" Various implementations of deque.

A deque is a double-ended queue, which supports adding + removing elements
from EITHER end.

>>> deque_add_right('d')
deque(['a', 'b', 'c', 'd'])

>>> deque_add_mult_right('def')
deque(['a', 'b', 'c', 'd', 'e', 'f'])
"""

from collections import deque


def deque_add_right(char_to_add):
    """Exploring Python's built-in deque. Add one to right."""

    d = deque('abc')
    d.append(char_to_add)

    return d


def deque_add_mult_right(char_to_add):
    """Exploring Python's built-in deque. Add multiple to right."""

    d = deque('abc')
    d.extend(char_to_add)

    return d




# def deque_add_left():
#     """Exploring Python's built-in deque. Add to left."""


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "All tests passed!"
