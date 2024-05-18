
import unittest
import heapq
from HW8.cables_cost import *

class TestMinCostToConnectCables(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(min_cost_to_connect_cables([4, 3, 2, 6]), 29)
    
    def test_single_cable(self):
        self.assertEqual(min_cost_to_connect_cables([5]), 0)
    
    def test_two_cables(self):
        self.assertEqual(min_cost_to_connect_cables([1, 2]), 3)
    
    def test_three_cables(self):
        self.assertEqual(min_cost_to_connect_cables([1, 2, 3]), 9)
    
    def test_equal_length_cables(self):
        self.assertEqual(min_cost_to_connect_cables([4, 4, 4, 4]), 32)
    
    def test_increasing_length_cables(self):
        self.assertEqual(min_cost_to_connect_cables([1, 2, 3, 4, 5]), 33)

if __name__ == '__main__':
    unittest.main()