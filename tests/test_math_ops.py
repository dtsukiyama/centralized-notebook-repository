import pytest
import numpy as np
from utils.math_ops import add, multiply


def test_add():
    assert add(2, 3) == 5  # Adding scalars
    assert np.array_equal(add([1, 2], [3, 4]), [4, 6])  # Element-wise addition


def test_multiply():
    assert multiply(2, 3) == 6  # Multiplying scalars
    assert np.array_equal(
        multiply([1, 2], [3, 4]), [3, 8]
    )  # Element-wise multiplication
