import pytest
from utils.math_ops import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add([1, 2], [3, 4]) == [4, 6]  # Supports lists via NumPy or pandas

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply([1, 2], [3, 4]) == [3, 8]  # Supports lists via NumPy or pandas