import pytest
from AVL_tree import *

def test_find_largest():
    avl_tree = AVLTree()

    avl_tree.insert_value(10)
    avl_tree.insert_value(5)
    avl_tree.insert_value(15)
    avl_tree.insert_value(3)
    avl_tree.insert_value(7)
    avl_tree.insert_value(12)
    avl_tree.insert_value(17)

    # Find the largest value
    largest_value = avl_tree.find_largest()

    # Assert that the largest value is as expected
    assert largest_value == 17

def test_find_smallest():
    avl_tree = AVLTree()

    avl_tree.insert_value(10)
    avl_tree.insert_value(5)
    avl_tree.insert_value(15)
    avl_tree.insert_value(3)
    avl_tree.insert_value(7)
    avl_tree.insert_value(12)
    avl_tree.insert_value(17)

    # Find the smallest value
    smallest_value = avl_tree.find_smallest()

    # Assert that the smallest value is as expected
    assert smallest_value == 3

def test_sum_values():
    # Create an instance of AVLTree
    avl_tree = AVLTree()

    # Test case for an empty AVL tree
    assert avl_tree.sum_values() == 0  # Expected sum of values is 0 for an empty tree

    # Insert one value into the AVL tree
    avl_tree.insert_value(10)
    # Test case for AVL tree with only one node
    assert avl_tree.sum_values() == 10  # Expected sum of values is the value of the single node (10)

    # Insert more values into the AVL tree
    avl_tree.insert_value(5)
    avl_tree.insert_value(15)
    avl_tree.insert_value(3)
    avl_tree.insert_value(7)
    avl_tree.insert_value(12)
    avl_tree.insert_value(17)

    # Calculate the sum of all values
    total_sum = avl_tree.sum_values()

    # Assert that the total sum is as expected
    assert total_sum == 69


if __name__ == "__main__":
    pytest.main()