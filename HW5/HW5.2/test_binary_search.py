
import pytest
from binary_search import binary_search

def test_exact_match():
    arr = [0.1, 1.5, 2.2, 3.3, 4.4, 5.5]
    target = 3.3
    iterations, upper_bound = binary_search(arr, target)
    assert upper_bound == target, "Upper bound should be the target itself when an exact match is found"

def test_no_exact_match_greater():
    arr = [0.1, 1.5, 2.2, 3.3, 4.4, 5.5]
    target = 3.5
    iterations, upper_bound = binary_search(arr, target)
    assert upper_bound == 4.4, "Upper bound should be the smallest element greater than the target"

def test_no_exact_match_less():
    arr = [0.1, 1.5, 2.2, 3.3, 4.4, 5.5]
    target = 0.05
    iterations, upper_bound = binary_search(arr, target)
    assert upper_bound == 0.1, "Upper bound should be the smallest element in the array"

def test_target_greater_than_all():
    arr = [0.1, 1.5, 2.2, 3.3, 4.4, 5.5]
    target = 6
    iterations, upper_bound = binary_search(arr, target)
    assert upper_bound is None, "Upper bound should be None if target is greater than all elements"

def test_empty_array():
    arr = []
    target = 1
    iterations, upper_bound = binary_search(arr, target)
    assert upper_bound is None, "Upper bound should be None if the array is empty"